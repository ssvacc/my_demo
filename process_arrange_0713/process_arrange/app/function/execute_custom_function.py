#    Copyright (c)  Fancyqube.com
#    @Author : niheng
#    @Date: 2023/3/16 下午4:50
#    @Description:
# -*- coding: utf-8 -*-
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ConstEnum import FuncProcessCode
from ReturnEnum import ReturnEnum
from app.function import execute_function
from app.function.common import post_json_param
from app.table.t_public_custom_function_param_model import t_public_custom_function_param as TPublicCustomFunctionParam
from app.table.t_public_custom_function_relevance_model import \
    t_public_custom_function_relevance as TPublicCustomFunctionRelevance

logger = logging.getLogger('django.func_process_app.function.execute_custom_function')
logger.setLevel(logging.DEBUG)


# 自动执行函数
@csrf_exempt
def run_simple_task_res(request):
    request_data = post_json_param(request)
    task_id = request_data.get('task_id')
    args_list = request_data.get('param_list')
    function_relevance_list = TPublicCustomFunctionRelevance.objects.filter(task_id=task_id).order_by('function_order')
    res = run_function(function_relevance_list, args_list)
    if res['code'] == ReturnEnum.ER_SUCCESS().code:
        args_list = res['data']
    else:
        return JsonResponse(res)
    custom_function_param_list = TPublicCustomFunctionParam.objects.filter(task_id=task_id) \
        .filter(type=FuncProcessCode.FUNCTION_PARAM_RETURN.value)

    return_dict = get_return_dict(args_list, custom_function_param_list)
    res = {"code": ReturnEnum.ER_SUCCESS().code,
           "msg": ReturnEnum.ER_SUCCESS().msg,
           "data": return_dict}
    return JsonResponse(res)


# 从参数字典中取出需要的返回值
def get_return_dict(args_list, custom_function_param_list):
    return_dict = {}
    for custom_function_param in custom_function_param_list:
        custom_function_param_dict = custom_function_param.object_to_dict()
        param_name = custom_function_param_dict['param_name']
        return_dict.update({param_name: args_list[param_name]})
    return return_dict


# 发现函数，运行函数
def run_function(function_relevance_list, args_list):
    request_data = dict()
    for relevance in function_relevance_list:
        request_data['function_id'] = relevance.function_id
        function_name = ''
        try:
            # 获取函数和函数名
            func_obj, function_name = execute_function.get_function_obj(**request_data)
        except:
            res = {"code": ReturnEnum.ER_FUNCTION_NOT_FOUND().code,
                   "msg": ReturnEnum.ER_FUNCTION_NOT_FOUND().msg + function_name,
                   "data": None}
            return res
        try:
            # 运行函数，对内部多个小函数不做参数返回值校验，默认函数是调试通过的
            fun_res = func_obj(**args_list)
        except Exception as e:
            import traceback
            traceback.print_exc()
            res = {'code': ReturnEnum.ER_FAIL().code, 'msg': function_name + '函数执行出错!', 'data': None}
            return res
        # 更新执行结果到参数对象
        if fun_res['code'] == ReturnEnum.ER_SUCCESS().code:
            args_list.update(fun_res['data'])
        else:
            res = {'code': ReturnEnum.ER_INTERFACE_FUNCTION_ERROR().code,
                   'msg': function_name + ReturnEnum.ER_INTERFACE_FUNCTION_ERROR().msg, 'data': fun_res}
            return res
    res = {'code': ReturnEnum.ER_SUCCESS().code, 'msg': ReturnEnum.ER_SUCCESS().msg, 'data': args_list}
    return res
