# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ConstEnum import FuncProcessCode
from ReturnEnum import ReturnEnum
from app.function import common
from app.function.common import post_json_param
from app.table.t_public_custom_function_log_model import t_public_custom_function_log as TPublicCustomFunctionLog
from app.table.t_public_function_model import t_public_function as TPublicFunction
from app.table.t_public_class_model import t_public_class as TPublicClass


# 新增类唯一校验
def class_add_unique(request_data):
    class_name = request_data.get('class_name', '')
    if class_name:
        class_name = class_name.strip()
    count = TPublicClass.objects.filter(class_name=class_name).count()
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    if count > 0:
        res = {'code': ReturnEnum.ER_FAIL().code, 'msg': '新增失败：' + class_name + "已存在!"}
    return count == 0, res


# 校验类是否被引用
def check_class_used(class_id):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    clazz = TPublicClass.objects.filter(id=class_id).first()
    # 校验类是否被其他函数引用
    function_name_start = clazz.class_name + FuncProcessCode.CLASS_NAME_SEPARATE.value
    class_function_count = TPublicFunction.objects.filter(function_name__startswith=function_name_start).count()
    if class_function_count > 0:
        res = {"code": ReturnEnum.ER_FAIL().code, "msg": "删除失败,该类已被函数使用", "data": None}
    return res


# 新增类
def class_add(request_data, first_name):
    class_name = request_data.get('class_name', '')
    if class_name:
        class_name = class_name.strip()
    class_desc = request_data.get('class_desc', '')
    if class_desc:
        class_desc = class_desc.strip()
    class_detail = request_data.get('class_detail', '')
    if class_detail:
        class_detail = class_detail.strip()
    clazz = TPublicClass(class_name=class_name, class_desc=class_desc, class_detail=class_detail)
    clazz.create_person = first_name
    clazz.create_time = common.getNowTimeStamp()
    clazz.save()
    # 记录日志
    param_log = TPublicCustomFunctionLog(table_id=clazz.id, action_user=first_name,
                                         table_type=FuncProcessCode.LOG_CLASS.value,
                                         action_type=FuncProcessCode.LOG_TYPE_ADD.value,
                                         new_name=request_data.get('class_name'),
                                         new_desc=request_data.get('class_desc'),
                                         action_time=common.getNowTimeStamp())
    param_log.save()


# 编辑类
def class_update(request_data, first_name):
    class_id = request_data.get('id')
    clazz = TPublicClass.objects.get(id=class_id)
    new_name = request_data.get('class_name', '')
    if new_name:
        new_name = new_name.strip()
    old_name = clazz.class_name
    old_desc = clazz.class_desc
    clazz.class_name = new_name
    new_desc = request_data.get('class_desc', '')
    if new_desc:
        new_desc = new_desc.strip()
    clazz.class_desc = new_desc
    class_detail = request_data.get('class_detail', '')
    if class_detail:
        class_detail = class_detail.strip()
    clazz.class_detail = class_detail
    clazz.save()
    # 记录日志
    param_log = TPublicCustomFunctionLog(table_id=class_id, old_name=old_name, old_desc=old_desc,
                                         action_user=first_name,
                                         new_name=new_name,
                                         new_desc=new_desc,
                                         action_time=common.getNowTimeStamp(),
                                         table_type=FuncProcessCode.LOG_CLASS.value,
                                         action_type=FuncProcessCode.LOG_TYPE_UPDATE.value)
    param_log.save()


# 新增类封装
@csrf_exempt
def class_add_res(request):
    request_data = post_json_param(request)
    flag, res = class_add_unique(request_data)
    if not flag:
        return JsonResponse(res)
    first_name = common.get_first_name(request)
    class_add(request_data, first_name)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "新增成功!", "data": None}
    return JsonResponse(res)


# 编辑类封装
@csrf_exempt
def class_update_res(request):
    request_data = post_json_param(request)
    first_name = common.get_first_name(request)
    class_update(request_data, first_name)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "操作成功!", "data": None}
    return JsonResponse(res)


# 删除类封装
@csrf_exempt
def class_del_res(request):
    request_data = post_json_param(request)
    first_name = common.get_first_name(request)
    class_id = request_data.get('id')
    res = check_class_used(class_id)
    if res['code'] == ReturnEnum.ER_SUCCESS().code:
        clazz = TPublicClass.objects.filter(id=class_id).first()
        # 记录日志
        param_log = TPublicCustomFunctionLog(table_id=class_id, old_name=clazz.class_name,
                                             old_desc=clazz.class_desc, action_user=first_name,
                                             action_time=common.getNowTimeStamp(),
                                             table_type=FuncProcessCode.LOG_CLASS.value,
                                             action_type=FuncProcessCode.LOG_TYPE_DEL.value)
        param_log.save()
        clazz.delete()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "删除成功!", "data": None}
    return JsonResponse(res)


# 不分页查询类封装
@csrf_exempt
def class_list_res(request):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    class_list = TPublicClass.objects.all().order_by('class_name')
    dict_list = []
    for clazz in class_list:
        dict_data = clazz.object_to_dict()
        dict_list.append(dict_data)
    res["data"] = dict_list
    return JsonResponse(res)
