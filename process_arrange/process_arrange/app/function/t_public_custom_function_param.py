# -*- coding: utf-8 -*-
from django.http import JsonResponse

from ConstEnum import FuncProcessCode
from ReturnEnum import ReturnEnum
from app.table.t_public_custom_function_param_model import t_public_custom_function_param as TPublicCustomFunctionParam
from app.table.t_public_params_model import t_public_params as TPublicParams


# 新增流程同步新增流程参数
def custom_function_param_add(task_id, param_id_list, param_type):
    custom_function_param_list = []
    for param_id in param_id_list:
        param = TPublicParams.objects.filter(id=param_id).first()
        custom_function_param_list.append(TPublicCustomFunctionParam(task_id=task_id,
                                                                     param_id=param.id,
                                                                     param_name=param.param_name,
                                                                     param_desc=param.param_desc,
                                                                     data_type=param.data_type,
                                                                     type=param_type))
    if len(custom_function_param_list) > 0:
        TPublicCustomFunctionParam.objects.bulk_create(custom_function_param_list)


# 修改流程参数，校验有变化，则先删后插
def custom_function_param_update(task_id, param_id_list, param_type):
    flag = check_param_change(task_id, param_id_list, param_type)
    if flag:
        # 对参数做了修改，则先删后插
        TPublicCustomFunctionParam.objects.filter(task_id=task_id).filter(type=param_type).delete()
        custom_function_param_add(task_id, param_id_list, param_type)


# 校验参数是否做了修改
def check_param_change(task_id, param_list, param_type):
    param_type_list = TPublicCustomFunctionParam.objects.filter(task_id=task_id).filter(type=param_type)
    param_id_list = []
    for func_param in param_type_list:
        param_id_list.append(func_param.param_id)
    flag = False
    for in_param_id in param_list:
        if in_param_id not in param_id_list:
            flag = True
    for db_id in param_id_list:
        if db_id not in param_list:
            flag = True
    return flag


# 根据功能id删除
def delete_by_task_id(task_id):
    TPublicCustomFunctionParam.objects.filter(task_id=task_id).delete()


# 根据功能id查询函数
def query_param_by_task_id(task_id):
    task_id = int(task_id)
    param_list = TPublicCustomFunctionParam.objects.filter(task_id=task_id).order_by('id')
    dict_list = []
    for param in param_list:
        dict_data = param.object_to_dict()
        dict_list.append(dict_data)
    return dict_list


# 根据功能id查询参数
def query_param_result_by_task_id(task_id):
    task_id = int(task_id)
    param_list = TPublicCustomFunctionParam.objects.filter(task_id=task_id)
    param_dict_list = []
    return_dict_list = []
    for param in param_list:
        dict_data = param.object_to_dict()
        # public_param = TPublicParams.objects.filter(id=param.param_id).first()
        # param_dict = public_param.object_to_dict()
        # loop_index = 0
        # dict_data = t_public_params.f_get_child_param(param_dict, loop_index)
        if param.type == FuncProcessCode.FUNCTION_PARAM_PARAM.value:
            param_dict_list.append(dict_data)
        else:
            return_dict_list.append(dict_data)
    return param_dict_list, return_dict_list


# 根据功能id查询函数封装
def query_by_task_id_res(request):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": None}
    result_list = query_param_by_task_id(request.GET.get('task_id'))
    res["data"] = result_list
    return JsonResponse(res)
