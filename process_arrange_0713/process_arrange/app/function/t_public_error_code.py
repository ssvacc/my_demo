# -*- coding: utf-8 -*-
import importlib
import inspect

from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ConstEnum import FuncProcessCode
from ReturnEnum import ReturnEnum
from app.function import common
from app.function.common import post_json_param
from app.table.t_public_custom_function_log_model import t_public_custom_function_log as TPublicCustomFunctionLog
from app.table.t_public_error_code_model import t_public_error_code as TPublicErrorCode
from app.table.t_public_function_param_model import t_public_function_param as TPublicFunctionParam


# 新增返回码
def error_code_add(request_data, first_name):
    status = FuncProcessCode.RETURN_ENUM_NO_ACTIVATE.value
    timestamp = common.getNowTimeStamp()
    error_code = TPublicErrorCode(name=request_data.get('name'),
                                  code=request_data.get('code'),
                                  msg=request_data.get('msg'),
                                  author=request_data.get('author'),
                                  status=status,
                                  create_time=timestamp)
    error_code.save()
    # 记录日志
    error_code_log = TPublicCustomFunctionLog(table_id=error_code.id, action_user=first_name,
                                              table_type=FuncProcessCode.LOG_ERROR_CODE.value,
                                              action_type=FuncProcessCode.LOG_TYPE_ADD.value,
                                              new_name=request_data.get('name'),
                                              new_desc=request_data.get('msg'),
                                              action_time=common.getNowTimeStamp())
    error_code_log.save()


# 编辑返回码
def error_code_update(request_data, first_name):
    error_code_id = request_data.get('id')
    error_code = TPublicErrorCode.objects.get(id=error_code_id)
    old_name = error_code.name
    old_msg = error_code.msg
    error_code.msg = request_data.get('msg')
    error_code.author = request_data.get('author')
    error_code.update_time = common.getNowTimeStamp()
    error_code.save()
    # 记录日志
    error_code_log = TPublicCustomFunctionLog(table_id=error_code_id, old_name=old_name, old_desc=old_msg,
                                              action_user=first_name,
                                              new_name=request_data.get('name'),
                                              new_desc=request_data.get('msg'),
                                              action_time=common.getNowTimeStamp(),
                                              table_type=FuncProcessCode.LOG_ERROR_CODE.value,
                                              action_type=FuncProcessCode.LOG_TYPE_UPDATE.value)
    error_code_log.save()


# 查询返回码
def error_code_list(request):
    condition = request.GET.get('condition', '').strip()
    q = TPublicErrorCode.objects
    if condition is not None:
        q = q.filter(Q(code__contains=condition) | Q(msg__contains=condition)
                     | Q(name__contains=condition) | Q(author__contains=condition))
    else:
        q = q.all()
    return q.order_by('code')


# 新增返回码封装
@csrf_exempt
def error_code_add_res(request):
    return common.add_res(None, error_code_add, request)


# 编辑返回码封装
@csrf_exempt
def error_code_update_res(request):
    return common.update_res(error_code_update, request)


# 删除返回码封装
@csrf_exempt
def error_code_del_res(request):
    if request.method != "POST":
        res = {'code': ReturnEnum.ER_FAIL().code, 'msg': 'Request Method Is Not Compared.', 'data': None}
        return JsonResponse(res)
    request_data = post_json_param(request)
    first_name = common.get_first_name(request)
    error_code_id = request_data.get('id')
    params_count = TPublicFunctionParam.objects.filter(code_id=error_code_id).count()
    if params_count == 0:
        t_public_error_code = TPublicErrorCode.objects.filter(id=error_code_id).first()
        # 记录日志
        error_code_log = TPublicCustomFunctionLog(table_id=error_code_id, old_name=t_public_error_code.name,
                                                  old_desc=t_public_error_code.msg, action_user=first_name,
                                                  action_time=common.getNowTimeStamp(),
                                                  table_type=FuncProcessCode.LOG_ERROR_CODE.value,
                                                  action_type=FuncProcessCode.LOG_TYPE_DEL.value)
        error_code_log.save()
        t_public_error_code.delete()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "删除成功!", "data": None}
    else:
        res = {"code": ReturnEnum.ER_FAIL().code, "msg": "删除失败,该返回码已被函数使用", "data": None}
    return JsonResponse(res)


# 不分页查询返回码封装
@csrf_exempt
def error_code_list_res(request):
    return common.list_res(error_code_list, request)



# 获取ReturnEnum文件中返回码
def get_file_error_code():
    module = importlib.import_module(FuncProcessCode.RETURN_ENUM_PATH.value)
    module_class = getattr(module, FuncProcessCode.RETURN_ENUM_CLASS_NAME.value)
    functions = inspect.getmembers(module_class)
    # 查询返回码
    cod_msg_collection = []
    for fun in functions:
        fun_name = fun[0]
        if not fun_name.startswith('__'):
            func_obj = getattr(module_class, fun_name)
            returnClass = func_obj()
            code = returnClass.code
            msg = returnClass.msg
            author = returnClass.author
            cod_msg = {"name": fun_name, "code": code, "msg": msg, "author": author}
            cod_msg_collection.append(cod_msg)
    return cod_msg_collection


# 获取ReturnEnum文件中返回码
def get_function_error_code(function_id):
    error_code_config = TPublicFunctionParam.objects.filter(type=FuncProcessCode.FUNCTION_PARAM_CODE.value) \
        .filter(function_id=function_id)
    code_id_list = []
    for error_code in error_code_config:
        code_id_list.append(error_code.code_id)
    code_list = TPublicErrorCode.objects.filter(id__in=code_id_list)
    return code_list


# 展示返回码源文件
def show_returnEnum_res(request):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": 'Success!', "data": None}
    # 获取ReturnEnum文件中返回码
    module = importlib.import_module(FuncProcessCode.RETURN_ENUM_PATH.value)
    module_class = getattr(module, FuncProcessCode.RETURN_ENUM_CLASS_NAME.value)
    resource = ''
    try:
        resource = inspect.getsource(module_class)
    except Exception as e:
        import traceback
        traceback.print_exc()
    res["data"] = resource
    return JsonResponse(res)


# # 返回码源文件增量同步到数据库
# def get_code_msg_from_file_res():
#     res = {"code": ReturnEnum.ER_SUCCESS().code,
#            "msg": 'Success!',
#            "data": None}
#     # 获取ReturnEnum文件中返回码
#     cod_msg_collection = get_file_error_code()
#     # 获取数据库中多返回码
#     all_code_msg = TPublicErrorCode.objects.all().order_by("name")
#     # 找到文件中比数据库中多的返回码
#     new_code_msg_list = []
#     for file_code in cod_msg_collection:
#         flag = True
#         for db_code in all_code_msg:
#             if file_code['name'] == db_code.name and str(file_code['code']) == str(db_code.code):
#                 flag = False
#                 break
#         if flag and file_code['name'].startswith(FuncProcessCode.BASE_CODE_PREFIX.value):
#             new_code_msg_list.append(file_code)
#     # 更新到数据库，状态设置为已发布
#     code_msg_list = []
#     for new_code_msg in new_code_msg_list:
#         di = dict()
#         code_msg = TPublicErrorCode(
#             name=new_code_msg['name'],
#             code=new_code_msg['code'],
#             msg=new_code_msg['msg'],
#             author=new_code_msg['author'],
#             create_time=common.getNowTimeStamp(),
#             status=FuncProcessCode.RETURN_ENUM_ACTIVATE.value)
#         di['key'] = new_code_msg['code']
#         di['value'] = code_msg
#         code_msg_list.append(di)
#     key_list = []
#     for x in code_msg_list:
#         key_list.append(x['key'])
#     key_list.sort()
#     print(key_list)
#     code_msg_list2 = []
#     for k in key_list:
#         for c in code_msg_list:
#             if k == c['key']:
#                 code_msg_list2.append(c['value'])
#                 break
#     print(code_msg_list2)
#     TPublicErrorCode.objects.bulk_create(code_msg_list2)
#     res["data"] = new_code_msg_list
#     return JsonResponse(res)


# 启动项目时检查文件中是否有配置的返回码，如果有，则将返回码状态置为1已发布
# 如果不是以ER_开头的，状态置为0草稿
def check_error_code_status():
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": 'Success!', "data": None}
    count = TPublicErrorCode.objects.filter(status=FuncProcessCode.RETURN_ENUM_NO_ACTIVATE.value).count()
    if count > 0:
        # 获取ReturnEnum文件中返回码
        cod_msg_collection = get_file_error_code()
        # 获取数据库中定义的返回码
        error_code_db_list = TPublicErrorCode.objects.filter(status=FuncProcessCode.RETURN_ENUM_NO_ACTIVATE.value)\
            .filter(name__startswith=FuncProcessCode.BASE_CODE_PREFIX.value)
        for error in error_code_db_list:
            error_code_dict = error.object_to_dict()
            for code_msg in cod_msg_collection:
                if error_code_dict['name'] == code_msg['name'] and str(error_code_dict['code']) == str(
                        code_msg['code']):
                    error.status = FuncProcessCode.RETURN_ENUM_ACTIVATE.value
                    error.author = code_msg['author']
                    error.msg = code_msg['msg']
                    error.update_time = common.getNowTimeStamp()
                    error.save()
                    break
    forbid_list = TPublicErrorCode.objects.filter(status=FuncProcessCode.RETURN_ENUM_ACTIVATE.value)\
        .exclude(name__startswith=FuncProcessCode.BASE_CODE_PREFIX.value)
    for item in forbid_list:
        item.status = FuncProcessCode.RETURN_ENUM_NO_ACTIVATE.value
        item.update_time = common.getNowTimeStamp()
        item.save()
    return JsonResponse(res)
