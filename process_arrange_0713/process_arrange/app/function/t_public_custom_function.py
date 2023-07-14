# -*- coding: utf-8 -*-
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from ConstEnum import FuncProcessCode, FuncProcessName
from ReturnEnum import ReturnEnum
from app.class_function.PageDemo import PageDemo
from app.function import common, t_public_custom_function_relevance, t_public_custom_function_param, t_public_function, \
    approve_comments
from app.page_function.GeneratePage import GeneratePage
from app.table.t_public_custom_function_log_model import t_public_custom_function_log as TPublicCustomFunctionLog
from app.table.t_public_custom_function_model import t_public_custom_function as TPublicCustomFunction, \
    taskResultChoices, scheduledChoices

from app.table.t_public_custom_function_relevance_model import t_public_custom_function_relevance \
    as TPublicCustomFunctionRelevance
from app.table.t_public_error_code_model import t_public_error_code as TPublicErrorCode
from app.table.t_public_function_model import t_public_function as TPublicFunction
from app.table.t_public_function_param_model import t_public_function_param as TPublicFunctionParam
from app.table.t_public_custom_function_param_model import t_public_custom_function_param as TPublicCustomFunctionParam


# 新增流程唯一校验
def custom_function_add_unique(request_data):
    task_name = request_data.get('task_name')
    task_desc = request_data.get('task_desc')
    count_task_name = TPublicCustomFunction.objects.filter(task_name=task_name).count()
    count_task_desc = 0
    res = ReturnEnum.ER_SUCCESS()
    if count_task_name > 0:
        res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
               'msg': task_name + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg}
    else:
        count_task_desc = TPublicCustomFunction.objects.filter(task_desc=task_desc).count()
        if count_task_desc > 0:
            res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
                   'msg': task_desc + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg}
    return count_task_name == 0 and count_task_desc == 0, res


# 编辑流程唯一校验
def custom_function_update_unique(request_data):
    task_id = request_data.get('id')
    task_name = request_data.get('task_name')
    task_desc = request_data.get('task_desc')
    count_task_name = TPublicCustomFunction.objects.filter(Q(task_name=task_name) & ~Q(id=task_id)).count()
    count_task_desc = 0
    res = ReturnEnum.ER_SUCCESS()
    if count_task_name > 0:
        res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
               'msg': task_name + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg}
    else:
        count_task_desc = TPublicCustomFunction.objects.filter(Q(task_desc=task_desc) & ~Q(id=task_id)).count()
        if count_task_desc > 0:
            res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
                   'msg': task_desc + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg}
    return count_task_name == 0 and count_task_desc == 0, res


# 新增流程
def custom_function_add(request_data, first_name):
    function_id_list = request_data.get('function_id_list')
    if function_id_list is None:
        return
    timestamp = common.getNowTimeStamp()
    task_test_result = taskResultChoices[2][0]
    scheduled_tasks = scheduledChoices[0][0]
    custom_function = TPublicCustomFunction(
        task_name=request_data.get('task_name'),
        task_desc=request_data.get('task_desc'),
        task_detail=request_data.get('task_detail'),
        task_test_result=task_test_result,
        scheduled_tasks=scheduled_tasks,
        status=FuncProcessCode.STATUS_NO_ACTIVATE.value,
        create_person=first_name,
        create_time=timestamp)
    custom_function.save()
    if custom_function.id is None:
        return
    if function_id_list:
        t_public_custom_function_relevance.custom_function_relevance_add(custom_function.id, function_id_list)
    param_id_list = request_data.get('param_id_list')
    return_id_list = request_data.get('return_id_list')
    t_public_custom_function_param.custom_function_param_add(custom_function.id, param_id_list,
                                                             FuncProcessCode.FUNCTION_PARAM_PARAM.value)
    t_public_custom_function_param.custom_function_param_add(custom_function.id, return_id_list,
                                                             FuncProcessCode.FUNCTION_PARAM_RETURN.value)

    # 记录日志
    param_log = TPublicCustomFunctionLog(table_id=custom_function.id, new_name=custom_function.task_name,
                                         new_desc=custom_function.task_detail, action_user=first_name,
                                         action_time=common.getNowTimeStamp(),
                                         table_type=FuncProcessCode.LOG_CUSTOM_FUNCTION.value,
                                         action_type=FuncProcessCode.LOG_TYPE_ADD.value)
    param_log.save()


# 编辑流程
def custom_function_update(request_data, first_name):
    update_time = common.getNowTimeStamp()
    task_name = request_data.get('task_name')
    task_desc = request_data.get('task_desc')
    task_detail = request_data.get('task_detail')
    task_config_node = request_data.get('task_config_node')
    task_config_link = request_data.get('task_config_link')
    task_test_result = request_data.get('task_test_result')
    function_id_list = request_data.get('function_id_list')
    param_id_list = request_data.get('param_id_list')
    return_id_list = request_data.get('return_id_list')
    status = request_data.get('status')
    task_id = request_data.get('id')
    custom_function = TPublicCustomFunction.objects.get(id=task_id)
    old_name = custom_function.task_name
    old_desc = custom_function.task_detail
    custom_function.update_time = update_time
    if task_name:
        custom_function.task_name = task_name
    if task_desc:
        custom_function.task_desc = task_desc
    if task_detail:
        custom_function.task_detail = task_detail
    if task_config_node:
        custom_function.task_config_node = task_config_node
    if task_config_link:
        custom_function.task_config_link = task_config_link
    if task_test_result:
        custom_function.task_test_result = request_data.get('task_test_result')
    if custom_function.status == FuncProcessCode.STATUS_NO_ACTIVATE.value:
        t_public_custom_function_relevance.custom_function_relevance_update(task_id, function_id_list)
        t_public_custom_function_param.custom_function_param_update(task_id, param_id_list,
                                                                    FuncProcessCode.FUNCTION_PARAM_PARAM.value)
        t_public_custom_function_param.custom_function_param_update(task_id, return_id_list,
                                                                    FuncProcessCode.FUNCTION_PARAM_RETURN.value)
    if status:
        custom_function.status = request_data.get('status')
    custom_function.save()

    # 记录日志
    param_log = TPublicCustomFunctionLog(table_id=task_id, old_name=old_name, old_desc=old_desc,
                                         action_user=first_name,
                                         new_name=task_name, new_desc=task_detail,
                                         action_time=common.getNowTimeStamp(),
                                         table_type=FuncProcessCode.LOG_CUSTOM_FUNCTION.value,
                                         action_type=FuncProcessCode.LOG_TYPE_UPDATE.value)
    param_log.save()


# 删除流程
def custom_function_del(request_data, first_name):
    task_id = request_data.get('id')
    # 待删除功能
    t_task = TPublicCustomFunction.objects.filter(id=task_id).first()
    # 删除功能函数，删除功能参数
    t_public_custom_function_relevance.delete_by_task_id(task_id)
    t_public_custom_function_param.delete_by_task_id(task_id)
    # 记录日志
    param_log = TPublicCustomFunctionLog(table_id=task_id, old_name=t_task.task_name,
                                         old_desc=t_task.task_detail, action_user=first_name,
                                         action_time=common.getNowTimeStamp(),
                                         table_type=FuncProcessCode.LOG_CUSTOM_FUNCTION.value,
                                         action_type=FuncProcessCode.LOG_TYPE_DEL.value)
    param_log.save()
    # 删除功能
    t_task.delete()


# 根据id查询流程
def custom_function_getById(request):
    function_id = request.GET.get('id')
    return TPublicCustomFunction.objects.get(id=function_id)


# functions = functions.objects.all()[page_no:page_size]
# 分页查询流程
def custom_function_page_list(request, page_no, page_size):
    condition = request.GET.get('condition', '').strip()
    query = TPublicCustomFunction.objects
    status = request.GET.get('status')
    if status:
        # 状态精准匹配
        query = query.filter(status=status)
    if condition == FuncProcessCode.COMMENT_NO_READ_DESC.value:
        custom_id_list = approve_comments.get_no_comment_list(FuncProcessName.PUBLIC_CUSTOM_FUNCTION_CN.value, common.get_first_name(request))
        query = query.filter(id__in=custom_id_list)
    elif condition:
        # 参数，返回值精准匹配
        task_param_list = TPublicCustomFunctionParam.objects.filter(Q(param_name=condition) | Q(param_desc=condition))
        if len(task_param_list) > 0:
            task_id_list = []
            for param in task_param_list:
                task_id_list.append(param.task_id)
            query = query.filter(id__in=task_id_list)
        else:
            # 函数中英文名精准匹配
            function_list = TPublicFunction.objects.filter(Q(function_name=condition) | Q(function_desc=condition))
            if len(function_list) > 0:
                function_id_list = []
                for function in function_list:
                    function_id_list.append(function.id)
                release_list = TPublicCustomFunctionRelevance.objects.filter(function_id__in=function_id_list)
                task_id_list = []
                for release in release_list:
                    task_id_list.append(release.task_id)
                query = query.filter(id__in=task_id_list)
            else:
                # 字段模糊匹配
                query = query.filter(Q(create_person=condition) | Q(release_person=condition)
                                     | Q(task_name__icontains=condition) | Q(task_desc__contains=condition)
                                     | Q(task_detail__contains=condition))
    task_list = query.order_by('-release_time', '-id')
    page_data, page_info = common.custom_paginator(task_list, page_no, page_size)

    # 查询当前页函数的参数和返回值
    if page_data:
        for item in page_data:
            function_relevance_list = TPublicCustomFunctionRelevance.objects.filter(task_id=item.id)
            function_id_list = []
            for func in function_relevance_list:
                function_id_list.append(func.function_id)
            # 查询当前页函数的参数和返回值具体内容 todo:mysql in 查询会对id重新排序，这里应该不排序
            # function_list = TPublicFunction.objects.filter(id__in=function_id_list)
            # 转为字典
            function_dict_list = []
            for function_id in function_id_list:
                function_data = TPublicFunction.objects.filter(id=function_id).first()
                t_public_function.stash_function_param_detail(function_data)
                function_dict_list.append(function_data.object_to_dict())
            item.function_list = function_dict_list
            param_dict_list, return_dict_list = t_public_custom_function_param.query_param_result_by_task_id(item.id)
            item.param_list = param_dict_list
            item.return_list = return_dict_list
    page = {'total': page_info['object_count'], 'data': page_data}
    return page


# 根据功能id查询返回码
def query_error_code_by_task_id(task_id):
    task_id = int(task_id)
    function_relevance_list = TPublicCustomFunctionRelevance.objects.filter(task_id=task_id)
    function_id_list = []
    for function_relevance in function_relevance_list:
        function_id_list.append(function_relevance.function_id)
    function_code_list = TPublicFunctionParam.objects.filter(function_id__in=function_id_list)\
        .filter(type=FuncProcessCode.FUNCTION_PARAM_CODE.value)
    code_id_list = []
    for code in function_code_list:
        code_id_list.append(code.code_id)
    error_code_list = TPublicErrorCode.objects.filter(id__in=code_id_list)
    dict_data_list = []
    for error_code in error_code_list:
        dict_data = error_code.object_to_dict()
        dict_data_list.append(dict_data)
    return dict_data_list


# 新增流程封装
@csrf_exempt
def custom_function_add_res(request):
    request_data = common.post_json_param(request)
    flag, res = custom_function_add_unique(request_data)
    if not flag:
        return JsonResponse(res)
    first_name = common.get_first_name(request)
    custom_function_add(request_data, first_name)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "新增成功!", "data": None}
    return JsonResponse(res)


# 编辑流程封装
@csrf_exempt
def custom_function_update_res(request):
    request_data = common.post_json_param(request)
    flag, res = custom_function_update_unique(request_data)
    if not flag:
        return JsonResponse(res)
    first_name = common.get_first_name(request)
    custom_function_update(request_data, first_name)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "操作成功!", "data": None}
    return JsonResponse(res)


# 删除流程封装
@csrf_exempt
def custom_function_del_res(request):
    return common.del_res(custom_function_del, request)


# 根据id查询流程数封装
def custom_function_get_by_id_res(request):
    return common.get_by_id_res(custom_function_getById, request)


# 分页查询流程封装
def custom_function_list_res(request):
    return common.page_res(custom_function_page_list, request)


# 函数配置保存接口
@csrf_exempt
def custom_function_config_res(request):
    if "POST" != request.method:
        res = {'code': ReturnEnum.ER_FAIL().code, 'msg': 'Request Method Is Not Compared.'}
        return JsonResponse(res)
    request_data = common.post_json_param(request)
    first_name = common.get_first_name(request)
    # 配置信息存入功能表
    custom_function_update(request_data, first_name)


# 根据id取节点
def get_node_by_id(node_id, task_config_node_dict):
    for node in task_config_node_dict:
        if node['id'] == node_id:
            return node


# 根据功能id查询返回码
def custom_function_error_code_res(request):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": None}
    result_list = query_error_code_by_task_id(request.GET.get('task_id'))
    res["data"] = result_list
    return JsonResponse(res)


# 函数提交审核
def commit_custom_function(request):
    # 需要展开的参数id
    param_id = request.GET.get('id')
    status = int(request.GET.get('status'))
    first_name = common.get_first_name(request)
    t_custom_function = TPublicCustomFunction.objects.filter(id=param_id).first()
    # 状态是已发布，或者提交人不是创建人，提示没有相关权限
    if (t_custom_function.status == FuncProcessCode.STATUS_RELEASE.value
            or status == FuncProcessCode.STATUS_RELEASE.value) \
            or (t_custom_function.create_person and t_custom_function.create_person != first_name):
        res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg, "data": None}
    else:
        t_custom_function.status = status
        t_custom_function.save()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    return JsonResponse(res)


# 函数审核
def approve_custom_function(request):
    # 需要展开的参数id
    param_id = request.GET.get('id')
    status = int(request.GET.get('status'))
    is_approve, first_name = common.approve_person(request)
    t_custom_function = TPublicCustomFunction.objects.filter(id=param_id).first()
    # 不是审核人，提示没有相关权限
    if not is_approve:
        res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg, "data": None}
    else:
        t_custom_function.status = status
        # 撤销审核则将审核人和审核时间置为空
        if t_custom_function.status == FuncProcessCode.STATUS_RELEASE.value \
                and status == FuncProcessCode.STATUS_SUBMIT.value:
            t_custom_function.release_time = None
            t_custom_function.release_person = None
        else:
            t_custom_function.release_time = common.getNowTimeStamp()
            t_custom_function.release_person = first_name
        t_custom_function.save()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    return JsonResponse(res)


@csrf_exempt
def view_page(request):
    s_page_name = request.GET.get('page_name', '')
    # 获取生成页面的配置信息
    config_result = PageDemo.get_demo_config_select_area_container_bak0706(s_page_name)
    if config_result['code'] != ReturnEnum.ER_SUCCESS().code:
        return JsonResponse(config_result)
    s_page_template_config = config_result['data']['s_page_template_config']
    # 调用通用生成页面的函数(生成各个流程节点的子页面)
    result = GeneratePage.common_view_page_by_config_new_window(s_page_template_config, s_page_name)
    # s_page_name_en = ''
    # main_rendered_html = ''
    # if result['code'] == ReturnEnum.ER_SUCCESS().code:
    #     s_page_name_en = result['data']['s_vue_component_file_name']
    #     main_rendered_html = result['data']['s_vue_component_content']
    # return HttpResponse(main_rendered_html)
    return JsonResponse(result)