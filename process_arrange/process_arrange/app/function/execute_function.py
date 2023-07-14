#    Copyright (c)  Fancyqube.com
#    @Author : niheng
#    @Date: 2023/3/16 下午4:50
#    @Description:
# -*- coding: utf-8 -*-
import importlib
import inspect
import json
import logging
import os
import traceback
from django.db.models import Model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ConstEnum import FuncProcessCode
from ReturnEnum import ReturnEnum
from app.function import t_public_function_param, t_public_error_code, common
from app.table.t_public_function_model import t_public_function as TPublicFunction

logger = logging.getLogger('django.func_process_app.function.execute_function')
logger.setLevel(logging.DEBUG)

# 校验函数的参数
def check_function_param(var_name_list, var_param_config_list):
    for var_conf in var_param_config_list:
        if var_conf not in var_name_list:
            return False
    return True


# 校验函数的返回值,所有配置的返回值,必需在函数返回中找到(==> 改为 非ER_SUCCESS情况下，校验成功，ER_SUCCESS情况下不能比配置的返回值多)
def check_function_result(result, var_result_config_list):
    if not isinstance(result, dict):
        return False
    result_keys = result.keys()
    if 'code' not in result_keys or 'msg' not in result_keys and 'data' not in result_keys:
        return False
    code = result['code']
    if code != ReturnEnum.ER_SUCCESS().code:
        return True
    data = result['data']
    if not isinstance(data, dict):
        return False
    data_keys = data.keys()
    for key in data_keys:
        if key not in var_result_config_list:
            return False
    return True


# 校验函数的返回码
def check_function_error_code(result, code_config_list):
    if not isinstance(result, dict):
        return False
    result_keys = result.keys()
    if 'code' not in result_keys or 'msg' not in result_keys and 'data' not in result_keys:
        return False
    result_code = result['code']
    code_list = []
    for code in code_config_list:
        code_list.append(code.code)
    return result_code in code_list


# 获取函数(函数名，函数路径)
# func_name：函数名；例：function_list_res
# func_route：函数路径 ==> BASE_DIR + 文件路径 ；例：func_process_app.function.t_public_function
# request：request对象
# model_info： model路径 + model名
def get_function(func_name, func_route, request=None, model_info=None):
    if func_name.find("::") >= 0:
        class_name = func_name.split('::')[0].replace("()", "").strip()
        func_name = func_name.split('::')[-1].replace("()", "").strip()
    else:
        class_name = ""
        func_name = func_name.replace("()", "").strip()
    if class_name:
        admin_class = getattr(importlib.import_module(func_route), class_name)
        if request:
            admin_class.request = request
        if model_info:
            if isinstance(model_info, Model):
                model_class = model_info
            else:
                model_file_route = model_info.split('+')[0]
                model_class_name = model_info.split('+')[-1]
                model_class = getattr(importlib.import_module(model_file_route), model_class_name)
            admin_class.model = model_class
        func_obj = getattr(admin_class(), func_name)
    else:
        module = importlib.import_module(func_route)
        func_obj = getattr(module, func_name)
    return func_obj


# 获取函数(函数名，函数路径)
def get_function_default(func_name, func_route):
    return get_function(func_name, func_route, None, None)


# 自动执行函数封装
@csrf_exempt
def run_function_res(request):
    request_data = common.post_json_param(request)
    return run_function(**request_data)


# param_list : [参数1:值,参数2:值,...]
# 自动执行函数封装
@csrf_exempt
def run_function(**kwargs):
    res = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
    param_list = kwargs.get('param_list')
    function_id = kwargs.get('function_id')
    try:
        func_obj, function_name = get_function_obj(**kwargs)
    except Exception as e:
        res = {"code": ReturnEnum.ER_FUNCTION_NOT_FOUND().code,
               "msg": ReturnEnum.ER_FUNCTION_NOT_FOUND().msg,
               "data": None}
        return JsonResponse(res)
    # 判断接口函数有没有装饰器
    try:
        flag = hasattr(func_obj, '__wrapped__')
        if flag:
            # 有装饰器则使用接口函数装饰器做校验
            param_list.update({"interface_function_id": function_id})
            param_list.update({"interface_function_name": function_name})
            print('run_function:param_list')
            print(param_list)
            res = func_obj(**param_list)
        else:
            param_list.update({'function_id': function_id})
            param_list.update({'function_name': function_name})
            param_list.update({'func_obj': func_obj})
            res, function_run_time = auto_run_function(**param_list)
    except Exception as e:
        res['msg'] = traceback.format_exc()
    loop_index = 0
    common.deal_dict_json(res, loop_index)
    return JsonResponse(res)


def clear_args(**kwargs):
    if "function_id" in kwargs.keys():
        kwargs.pop('function_id')
    if "function_name" in kwargs.keys():
        kwargs.pop('function_name')
    if "func_obj" in kwargs.keys():
        kwargs.pop('func_obj')
    if "interface_function_id" in kwargs.keys():
        kwargs.pop('interface_function_id')
    if "interface_function_name" in kwargs.keys():
        kwargs.pop('interface_function_name')
    return kwargs


def auto_run_function(**kwargs):
    function_id = kwargs.get('function_id')
    function_name = kwargs.get('function_name')
    func_obj = kwargs.get('func_obj')
    kwargs = clear_args(**kwargs)
    # 获取函数的参数配置
    fun_param_config_list = t_public_function_param.query_param_by_function_id(function_id)
    # 对函数的入参名称进行校验
    var_param_config_list = []
    var_result_config_list = []
    for param_config in fun_param_config_list:
        if FuncProcessCode.FUNCTION_PARAM_PARAM.value == param_config['type']:
            var_param_config_list.append(param_config['param_name'])
        else:
            var_result_config_list.append(param_config['param_name'])
    check_param_res = check_function_param(func_obj.__code__.co_varnames, var_param_config_list)
    res = {"code": ReturnEnum.ER_PARAM_NOT_MATCH().code,
           "msg": function_name + ":" + ReturnEnum.ER_PARAM_NOT_MATCH().msg,
           "data": None}
    function_run_time = 0
    if check_param_res:
        try:
            start_run_time = common.now_time()
            fun_res = func_obj(**kwargs)
            end_run_time = common.now_time()
            function_run_time = end_run_time - start_run_time
        except Exception as ex:
            res = {'code': ReturnEnum.ER_FAIL().code, 'msg': '函数执行出错!' + traceback.format_exc(), 'data': dict()}
            return res
        try:
            check_result_result = check_function_result(fun_res, var_result_config_list)
            code_config_list = t_public_error_code.get_function_error_code(function_id)
            check_code_result = check_function_error_code(fun_res, code_config_list)
            if not check_result_result:
                res = {"code": ReturnEnum.ER_RESULT_NOT_MATCH().code,
                       "msg": function_name + ":" + ReturnEnum.ER_RESULT_NOT_MATCH().msg,
                       "data": None}
            elif not check_code_result:
                res = {"code": ReturnEnum.ER_CODE_NOT_MATCH().code,
                       "msg": function_name + ":" + ReturnEnum.ER_CODE_NOT_MATCH().msg,
                       "data": None}
            else:
                res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "运行成功!", "data": fun_res}
        except Exception as ex:
            res = {"code": ReturnEnum.ER_SERVER_ERROR().code,
                   "msg": function_name + ":" + ReturnEnum.ER_SERVER_ERROR().msg,
                   "data": None}
            return res
    return res, function_run_time



# 根据函数id找到可执行函数
def get_function_obj(**kwargs):
    func_route, function_name = get_svn_url_by_function_id(kwargs.get('function_id'))
    func_obj = get_function_default(function_name, func_route)
    return func_obj, function_name

# 根据函数名找到可执行函数
def get_function_by_name(s_function_name, **kwargs):
    if kwargs.get('s_function_name'):
        s_function_name = kwargs.get('s_function_name')
    t_pub_function = TPublicFunction.objects.filter(function_name=s_function_name).first()
    s_function_route = get_function_path(t_pub_function.url)
    obj_function = get_function_default(s_function_name, s_function_route)
    return obj_function

# 从函数配置库获取函数路径(相对路径)
def get_svn_url_by_function_id(function_id):
    # 获取函数配置
    t_pub_function = TPublicFunction.objects.get(id=function_id)
    function_name = t_pub_function.function_name
    func_route = get_function_path(t_pub_function.url)
    return func_route, function_name


def get_function_path(url):
    # svn路径改为相对路径
    base_dir = FuncProcessCode.SVN_BASE_URL.value
    func_route = ''
    if url.__contains__(base_dir):
        func_route = url.replace(base_dir, '')
        func_route = func_route.replace(os.sep, '.')
    if url.endswith('.py'):
        func_route = func_route.replace('.py', '')
    return func_route


# 从函数配置库获取函数路径(绝对路径)
def get_absolute_url_by_function_id(function_id):
    # 获取函数配置
    t_pub_function = TPublicFunction.objects.get(id=function_id)
    function_name = t_pub_function.function_name
    url = t_pub_function.url
    # 绝对路径改为相对路径
    from django.conf import settings
    base_dir = settings.BASE_DIR
    func_route = ''
    if url.__contains__(base_dir):
        func_route = url.replace(base_dir + os.sep, '')
        func_route = func_route.replace(os.sep, '.')
    if url.endswith('.py'):
        func_route = func_route.replace('.py', '')
    return func_route, function_name


# 从函数配置库获取函数路径(相对路径)
def get_relative_url_by_function_id(function_id):
    # 获取函数配置
    t_pub_function = TPublicFunction.objects.get(id=function_id)
    function_name = t_pub_function.function_name
    url = t_pub_function.url
    func_route = ''
    if url.endswith('.py'):
        func_route = url.replace('.py', '')
    return func_route, function_name


# 展示函数体代码
def show_function_code(request):
    res = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": None}
    function_id = request.GET.get('function_id')
    try:
        function_obj, function_name = get_function_obj(function_id=function_id)
    except Exception as e:
        import traceback
        traceback.print_exc()
        res['code'] = ReturnEnum.ER_FUNCTION_NOT_FOUND().code
        res['msg'] = ReturnEnum.ER_FUNCTION_NOT_FOUND().msg
        return JsonResponse(res)
    try:
        print(function_obj)
        resource = inspect.getsource(function_obj)
    except Exception as e:
        import traceback
        traceback.print_exc()
        res['code'] = ReturnEnum.ER_FUNCTION_NOT_FOUND().code
        res['msg'] = ReturnEnum.ER_FUNCTION_NOT_FOUND().msg
        return JsonResponse(res)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": resource}
    return JsonResponse(res)


# 自动化测试调用函数执行
@csrf_exempt
def auto_test_function(request):
    res = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict}
    request_data = common.post_json_param(request)
    function_name = request_data.get('function_name')
    kwargs = request_data.get('param_list')
    start_time = common.now_time()
    try:
        t_pub_function = TPublicFunction.objects.filter(function_name=function_name).first()
        path = get_function_path(t_pub_function.url)
        func_obj = get_function_default(function_name, path)
    except Exception as e:
        res = {"code": ReturnEnum.ER_FUNCTION_NOT_FOUND().code,
               "msg": ReturnEnum.ER_FUNCTION_NOT_FOUND().msg,
               "data": dict()}
        return JsonResponse(res)
    # 判断接口函数有没有装饰器
    try:
        flag = hasattr(func_obj, '__wrapped__')
        if flag:
            # 有装饰器则使用接口函数装饰器做校验
            kwargs.update({"interface_function_id": t_pub_function.id})
            kwargs.update({"interface_function_name": function_name})
            res = func_obj(**kwargs)
        else:
            kwargs.update({'function_id': t_pub_function.id})
            kwargs.update({'function_name': function_name})
            kwargs.update({'func_obj': func_obj})
            res, function_run_time = auto_run_function(**kwargs)
            loop_index = 0
            common.deal_dict_json(res, loop_index)
            end_time = common.now_time()
            total_time = end_time - start_time  # 总耗时
            check_time = total_time - function_run_time  # 校验耗时
            data = res['data']
            res['data'] = dict()
            res['data']['function_result'] = data
            res['data']['total_time'] = total_time
            res['data']['check_time'] = check_time
            res['data']['function_run_time'] = function_run_time
    except Exception as e:
        res['msg'] = traceback.format_exc()
    return JsonResponse(res)
