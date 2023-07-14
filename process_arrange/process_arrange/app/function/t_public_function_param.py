# -*- coding: utf-8 -*-
from django.http import JsonResponse

from ConstEnum import FuncProcessCode
from ReturnEnum import ReturnEnum
from app.table.t_public_function_param_model import t_public_function_param as TPublicFunctionParam
from app.table.t_public_params_model import t_public_params as TPublicParams


# 批量新增
def function_param_add(function_id, param_list, param_example_list, param_type):
    func_param_list = []
    for param_id in param_list:
        example = None
        required = None
        if param_example_list:
            for param_example in param_example_list:
                if param_id == param_example['id']:
                    if 'example' not in param_example.keys():
                        param_example['example'] = None
                    example = param_example['example']
                    required = param_example['required']
        func_param = TPublicFunctionParam(function_id=function_id, param_id=param_id,
                                          example=example, required=required, type=param_type)
        func_param_list.append(func_param)
    TPublicFunctionParam.objects.bulk_create(func_param_list)


# 批量新增
def function_code_add(function_id, code_list, param_type):
    func_param_list = []
    for code_id in code_list:
        func_param = TPublicFunctionParam(function_id=function_id, code_id=code_id, type=param_type)
        func_param_list.append(func_param)
    TPublicFunctionParam.objects.bulk_create(func_param_list)


# 校验参数是否做了修改
def check_param_change(function_id, param_type, param_list):
    param_type_list = TPublicFunctionParam.objects.filter(function_id=function_id).filter(type=param_type)
    param_id_list = []
    for func_param in param_type_list:
        if param_type == FuncProcessCode.FUNCTION_PARAM_CODE.value:
            param_id_list.append(func_param.code_id)
        else:
            param_id_list.append(func_param.param_id)
    flag = False
    for in_param_id in param_list:
        if in_param_id not in param_id_list:
            flag = True
    for db_id in param_id_list:
        if db_id not in param_list:
            flag = True
    return flag


# 批量修改参数，返回值
def function_param_update(function_id, param_list, param_example_list, param_type):
    flag = check_param_change(function_id, param_type, param_list)
    if flag:
        # 对参数做了修改，则先删后插
        TPublicFunctionParam.objects.filter(function_id=function_id).filter(type=param_type).delete()
        function_param_add(function_id, param_list, param_example_list, param_type)



# 批量修改返回码
def function_code_update(function_id, code_list, param_type):
    flag = check_param_change(function_id, param_type, code_list)
    if flag:
        # 对返回码做了修改，则先删后插
        TPublicFunctionParam.objects.filter(function_id=function_id).filter(type=param_type).delete()
        function_code_add(function_id, code_list, param_type)


# 根据函数id查询参数
def query_param_by_function_id(function_id):
    function_id = int(function_id)
    data_type_list = [FuncProcessCode.FUNCTION_PARAM_PARAM.value,
                      FuncProcessCode.FUNCTION_PARAM_RETURN.value]
    function_param_list = TPublicFunctionParam.objects.filter(function_id=function_id) \
        .filter(type__in=data_type_list).order_by("id")
    dict_list = []
    for fun_param in function_param_list:
        if fun_param.type != FuncProcessCode.FUNCTION_PARAM_CODE.value:
            param = TPublicParams.objects.filter(id=fun_param.param_id).first()
            dict_data = param.object_to_dict()
            dict_data['type'] = fun_param.type
            dict_data['example'] = fun_param.example
            dict_data['required'] = fun_param.required
            dict_list.append(dict_data)
    return dict_list


# 根据函数id_list查询参数
def query_param_by_function_id_list(function_id_list, param_type):
    if not function_id_list:
        return []
    function_id_list = function_id_list.split(',')
    function_param_list = TPublicFunctionParam.objects.filter(function_id__in=function_id_list).order_by("id")
    param_id_list = []
    for fun_param in function_param_list:
        if fun_param.type == param_type:
            param_id_list.append(fun_param.param_id)
    dict_list = []
    param_id_set = set(param_id_list)
    param_list = TPublicParams.objects.filter(id__in=param_id_set)
    for param in param_list:
        dict_data = param.object_to_dict()
        dict_data['type'] = param_type
        dict_list.append(dict_data)
    return dict_list


# 批量修改示例值
def function_param_update_example(function_id, param_example_list):
    param_id_list = []
    if param_example_list:
        for param_example in param_example_list:
            param_id = param_example['id']
            param_id_list.append(param_id)
        function_param_list = TPublicFunctionParam.objects.filter(function_id=function_id) \
            .filter(param_id__in=param_id_list).filter(type=FuncProcessCode.FUNCTION_PARAM_PARAM.value)
        if len(function_param_list) > 0:
            for function_param in function_param_list:
                for param_example in param_example_list:
                    if 'example' not in param_example:
                        param_example['example'] = None
                    if function_param.param_id == param_example['id'] \
                            and (function_param.example != param_example['example']
                                 or function_param.required != param_example['required']):
                        function_param.example = param_example['example']
                        function_param.required = param_example['required']
                        function_param.save()


# 根据函数id删除
def delete_by_function_id(function_id):
    TPublicFunctionParam.objects.filter(function_id=function_id).delete()


# 根据函数id查询参数封装
def query_by_function_id_res(request):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": None}
    result_list = query_param_by_function_id(request.GET.get('function_id'))
    res["data"] = result_list
    return JsonResponse(res)


# 根据函数id查询参数封装
def query_by_custom_function_id_res(request):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": None}
    param_type = request.GET.get('type')
    if not param_type:
        param_type = FuncProcessCode.FUNCTION_PARAM_PARAM.value
    result_list = query_param_by_function_id_list(request.GET.get('function_id_list'), int(param_type))
    res["data"] = result_list
    return JsonResponse(res)
