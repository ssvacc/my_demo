# -*- coding: utf-8 -*-
from django.http import JsonResponse

from ReturnEnum import ReturnEnum
from app.table.t_public_custom_function_model import t_public_custom_function as TPublicCustomFunction
from app.table.t_public_custom_function_relevance_model import t_public_custom_function_relevance \
    as TPublicCustomFunctionRelevance


# 新增流程关系
def custom_function_relevance_add(task_id, function_id_list):
    custom_function_relevance_list = []
    for i in range(len(function_id_list)):
        function_id = function_id_list[i]
        custom_function_relevance = TPublicCustomFunctionRelevance(task_id=task_id, function_id=function_id,
                                                                   function_order=i + 1)
        custom_function_relevance_list.append(custom_function_relevance)
    TPublicCustomFunctionRelevance.objects.bulk_create(custom_function_relevance_list)


# 修改流程关系
def custom_function_relevance_update(task_id, function_id_list):
    flag = check_function_change(task_id, function_id_list)
    if flag:
        TPublicCustomFunctionRelevance.objects.filter(task_id=task_id).delete()
        custom_function_relevance_add(task_id, function_id_list)


# 校验函数是否做了修改
def check_function_change(task_id, function_id_list):
    function_db_list = TPublicCustomFunctionRelevance.objects.filter(task_id=task_id)
    function_db_id_list = []
    for function_db in function_db_list:
        function_db_id_list.append(function_db.function_id)
    flag = False
    for in_function_id in function_id_list:
        if in_function_id not in function_db_id_list:
            flag = True
    for db_id in function_db_id_list:
        if db_id not in function_id_list:
            flag = True
    return flag


# 根据功能id查询函数
def query_function_by_task_id(task_id):
    task_id = int(task_id)
    relevance_list = TPublicCustomFunctionRelevance.objects.filter(task_id=task_id).order_by('id')
    dict_list = []
    for relevance in relevance_list:
        func = TPublicCustomFunction.objects.filter(id=relevance.function_id).first()
        dict_data = func.object_to_dict()
        dict_list.append(dict_data)
    return dict_list


# 根据功能id删除
def delete_by_task_id(task_id):
    TPublicCustomFunctionRelevance.objects.filter(task_id=task_id).delete()


# 根据功能id查询函数封装
def query_by_task_id_res(request):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": None}
    result_list = query_function_by_task_id(request.GET.get('task_id'))
    res["data"] = result_list
    return JsonResponse(res)
