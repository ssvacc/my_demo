#    Copyright (c)  Fancyqube.com
#    @Author : niheng
#    @Date: 2023/3/16 下午4:50
#    @Description:
# -*- coding: utf-8 -*-
from ConstEnum import FuncProcessCode
from ReturnEnum import ReturnEnum
from app.function import execute_function
from app.table.t_public_custom_function_param_model import t_public_custom_function_param \
    as TPublicCustomFunctionParam
from app.table.t_public_function_model import t_public_function as TPublicFunction
from app.table.t_public_custom_function_model import t_public_custom_function as TPublicCustomFunction
from app.table.t_public_custom_function_relevance_model import \
    t_public_custom_function_relevance as TPublicCustomFunctionRelevance


# 根据流程名称执行流程函数
def fun_run_process(v_in_task_name, v_in_param_dict):
    res = {"code": ReturnEnum.ER_FAIL().code,
           "msg": ReturnEnum.ER_FAIL().msg,
           "data": dict()}
    custom_function = TPublicCustomFunction.objects.filter(task_name=v_in_task_name).first()
    if custom_function is None:
        # 没有流程，认为是个函数
        public_function = TPublicFunction.objects.filter(function_name=v_in_task_name).first()
        if public_function is None:
            res['code'] = ReturnEnum.ER_FUNCTION_NOT_FOUND().code
            res['msg'] = ReturnEnum.ER_FUNCTION_NOT_FOUND().msg + v_in_task_name
        else:
            res, v_in_param_dict = fun_execute_function(public_function.id, v_in_param_dict)
        return res
    function_relevance_list = TPublicCustomFunctionRelevance.objects.filter(task_id=custom_function.id)\
        .order_by('function_order')
    res = fun_execute_custom_function(function_relevance_list, v_in_param_dict)
    if res['code'] != ReturnEnum.ER_SUCCESS().code:
        return res
    args_list = res['data']
    custom_function_param_list = TPublicCustomFunctionParam.objects.filter(task_id=custom_function.id) \
        .filter(type=FuncProcessCode.FUNCTION_PARAM_RETURN.value)
    return_dict = fun_get_return_dict(args_list, custom_function_param_list)
    res['code'] = ReturnEnum.ER_SUCCESS().code
    res['msg'] = ReturnEnum.ER_SUCCESS().msg
    res['data'] = return_dict
    return res


# 发现函数，运行函数
def fun_execute_function(v_in_function_id, v_in_param_dict):
    request_data = dict()
    request_data['function_id'] = v_in_function_id
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
        res = func_obj(**v_in_param_dict)
    except Exception as e:
        res = {'code': ReturnEnum.ER_FAIL().code, 'msg': function_name + '函数执行出错!' + str(e), 'data': None}
        return res
    # 更新执行结果到参数对象
    if res['code'] == ReturnEnum.ER_SUCCESS().code:
        v_in_param_dict.update(res['data'])
    return res, v_in_param_dict


# 执行流程函数
def fun_execute_custom_function(v_in_function_relevance_list, v_in_param_dict):
    res = {'code': ReturnEnum.ER_FAIL().code, 'msg': ReturnEnum.ER_FAIL().msg, 'data': dict()}
    for relevance in v_in_function_relevance_list:
        fun_res, param_dict = fun_execute_function(relevance.function_id, v_in_param_dict)
        if fun_res['code'] == ReturnEnum.ER_SUCCESS().code:
            v_in_param_dict = param_dict
        else:
            return fun_res
    res['code'] = ReturnEnum.ER_SUCCESS().code
    res['msg'] = ReturnEnum.ER_SUCCESS().msg
    res['data'] = v_in_param_dict
    return res


# 流程结果集获取，从参数字典中取出需要的返回值
def fun_get_return_dict(v_in_args_list, v_in_custom_param_list):
    return_dict = {}
    for custom_function_param in v_in_custom_param_list:
        custom_function_param_dict = custom_function_param.object_to_dict()
        param_name = custom_function_param_dict['param_name']
        return_dict.update({param_name: v_in_args_list[param_name]})
    return return_dict
