# -*- coding: utf-8 -*-
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from ConstEnum import FuncProcessCode, FuncProcessName
from ReturnEnum import ReturnEnum
from app.class_function.PageFunction import PageFunction
from app.function import common, t_public_function_param, t_public_params, approve_comments
from app.table.t_public_custom_function_log_model import t_public_custom_function_log as TPublicCustomFunctionLog
from app.table.t_public_custom_function_relevance_model import t_public_custom_function_relevance \
    as TPublicCustomFunctionRelevance
from app.table.t_public_error_code_model import t_public_error_code as TPublicErrorCode
from app.table.t_public_page_function_model import t_public_page_function
from app.table.t_public_params_model import t_public_params as TPublicParams
from app.table.t_public_function_model import t_public_function as TPublicFunction
from app.table.t_public_function_param_model import t_public_function_param as TPublicFunctionParam


# 新增函数唯一校验
def function_add_unique(request_data):
    function_name = request_data.get('function_name')
    function_desc = request_data.get('function_desc')
    count_function_name = TPublicFunction.objects.filter(function_name=function_name).count()
    res = ReturnEnum.ER_SUCCESS()
    count_function_desc = 0
    if count_function_name > 0:
        res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
               'msg': function_name + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg,
               'data': None}
    else:
        count_function_desc = TPublicFunction.objects.filter(function_desc=function_desc).count()
        if count_function_desc > 0:
            res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
                   'msg': function_desc + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg,
                   'data': None}
    return count_function_name == 0 and count_function_desc == 0, res


# 编辑函数唯一校验
def function_update_unique(request_data):
    function_id = request_data.get('id')
    function_name = request_data.get('function_name')
    function_desc = request_data.get('function_desc')
    count_function_name = TPublicFunction.objects.filter(Q(function_name=function_name) & ~Q(id=function_id)).count()
    res = ReturnEnum.ER_SUCCESS()
    count_function_desc = 0
    if count_function_name > 0:
        res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
               'msg': function_name + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg,
               'data': None}
    else:
        count_function_desc = TPublicFunction.objects.filter(Q(function_desc=function_desc) & ~Q(id=function_id)).count()
        if count_function_desc > 0:
            res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
                   'msg': function_desc + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg,
                   'data': None}
    return count_function_name == 0 and count_function_desc == 0, res


# 新增函数
def function_add(request_data, first_name):
    timestamp = common.getNowTimeStamp()
    function = TPublicFunction(
        function_name=request_data.get('function_name'),
        function_desc=request_data.get('function_desc'),
        function_detail=request_data.get('function_detail'),
        author=first_name,
        s_principal=request_data.get('s_principal'),
        is_auto_test=FuncProcessCode.NO_AUTO_TEST.value,
        url=request_data.get('url'),
        status=FuncProcessCode.STATUS_NO_ACTIVATE.value,
        create_time=timestamp)
    if request_data.get('class_name'):
        function.class_name = request_data.get('class_name')
    function.save()
    if function.id is None:
        return
    param_list = request_data.get('param_list')
    param_example_list = request_data.get('param_example_list')
    return_list = request_data.get('return_list')
    error_code_list = request_data.get('error_code_list')
    if param_list is not None:
        t_public_function_param.function_param_add(function.id, param_list, param_example_list,
                                                   FuncProcessCode.FUNCTION_PARAM_PARAM.value)
    if return_list is not None:
        t_public_function_param.function_param_add(function.id, return_list, None,
                                                   FuncProcessCode.FUNCTION_PARAM_RETURN.value)
    if error_code_list is not None:
        t_public_function_param.function_code_add(function.id, error_code_list,
                                                  FuncProcessCode.FUNCTION_PARAM_CODE.value)
    # 记录日志
    param_log = TPublicCustomFunctionLog(table_id=function.id, new_name=function.function_name,
                                         new_desc=function.function_desc, action_user=first_name,
                                         action_time=common.getNowTimeStamp(),
                                         table_type=FuncProcessCode.LOG_FUNCTION.value,
                                         action_type=FuncProcessCode.LOG_TYPE_ADD.value)
    param_log.save()


# 编辑函数
def function_update(request_data, first_name):
    timestamp = common.getNowTimeStamp()
    function_id = request_data.get('id')
    def_function = TPublicFunction.objects.get(id=function_id)
    old_param = def_function.function_name
    old_desc = def_function.function_desc
    if request_data.get('function_name'):
        def_function.function_name = request_data.get('function_name')
    param_list = request_data.get('param_list')
    param_example_list = request_data.get('param_example_list')
    return_list = request_data.get('return_list')
    error_code_list = request_data.get('error_code_list')
    t_public_function_param.function_param_update(function_id, param_list, param_example_list,
                                                  FuncProcessCode.FUNCTION_PARAM_PARAM.value)
    t_public_function_param.function_param_update(function_id, return_list, None,
                                                  FuncProcessCode.FUNCTION_PARAM_RETURN.value)
    t_public_function_param.function_code_update(function_id, error_code_list,
                                                 FuncProcessCode.FUNCTION_PARAM_CODE.value)
    if request_data.get('url'):
        def_function.url = request_data.get('url')
    def_function.function_desc = request_data.get('function_desc')
    def_function.function_detail = request_data.get('function_detail')
    def_function.s_principal = request_data.get('s_principal')
    def_function.update_time = timestamp
    def_function.save()
    param_example_list = request_data.get('param_example_list')
    t_public_function_param.function_param_update_example(function_id, param_example_list)

    # 记录日志
    param_log = TPublicCustomFunctionLog(table_id=function_id, old_name=old_param, old_desc=old_desc,
                                         action_user=first_name,
                                         new_name=request_data.get('function_name'),
                                         new_desc=request_data.get('function_desc'),
                                         action_time=common.getNowTimeStamp(),
                                         table_type=FuncProcessCode.LOG_FUNCTION.value,
                                         action_type=FuncProcessCode.LOG_TYPE_UPDATE.value)
    param_log.save()


# 根据id查询函数
def function_getById(request):
    function_id = request.GET.get('id')
    return TPublicFunction.objects.get(id=function_id)


# functions = functions.objects.all()[page_no:page_size]
# 分页查询函数
def function_page_list(request, page_no, page_size):
    condition = request.GET.get('condition', '').strip()
    query = TPublicFunction.objects
    status = request.GET.get('status')
    class_name = request.GET.get('class_name', '').strip()
    if status:
        # 状态精准匹配
        query = query.filter(status=status)
        is_auto_test = request.GET.get('is_auto_test')
        if status == str(FuncProcessCode.STATUS_PUBLISH.value) and is_auto_test:
            query = query.filter(is_auto_test=is_auto_test)
    if class_name:
        # 类名精准匹配
        if class_name == FuncProcessCode.GLOBAL_FUNCTION_PREFIX.value:
            query = query.filter(Q(class_name__isnull=True) | Q(class_name=''))
        else:
            query = query.filter(class_name=class_name)
    if condition == FuncProcessCode.COMMENT_NO_READ_DESC.value:
        func_id_list = approve_comments.get_no_comment_list(FuncProcessName.PUBLIC_FUNCTION_CN.value, common.get_first_name(request))
        query = query.filter(id__in=func_id_list)
    elif condition:
        param_list = TPublicParams.objects.filter(Q(param_name=condition) | Q(param_desc=condition))
        error_code_list = TPublicErrorCode.objects.filter(Q(name=condition))
        if len(param_list) > 0:
            # 状态参数，返回值精准匹配
            query = condition_function_param(param_list, query, True)
        elif len(error_code_list) > 0:
            # 返回码精准匹配
            query = condition_function_param(error_code_list, query, False)
        else:
            # 字段模糊匹配，创建人，审核人，发布人，责任人精准匹配
            query = query.filter(Q(author=condition) | Q(release_person=condition)
                                 | Q(publish_person=condition) | Q(s_principal=condition)
                                 | Q(function_name__icontains=condition) | Q(function_desc__contains=condition)
                                 | Q(function_detail__contains=condition) | Q(url__contains=condition))
    function_list = query.order_by('-release_time', '-id')
    page_data, page_info = common.custom_paginator(function_list, page_no, page_size)
    # 查询当前页函数的参数和返回值
    if page_data is not None:
        for item in page_data:
            stash_function_param_detail(item)
    page = {'total': page_info['object_count'], 'data': page_data}
    return page


def condition_function_param(data_list, query, b_param_flag):
    data_id_list = []
    for data in data_list:
        data_id_list.append(data.id)
    if b_param_flag:
        function_param_list = TPublicFunctionParam.objects.filter(param_id__in=data_id_list)
    else:
        function_param_list = TPublicFunctionParam.objects.filter(code_id__in=data_id_list)
    function_id_list = []
    for function_param in function_param_list:
        function_id_list.append(function_param.function_id)
    query = query.filter(id__in=function_id_list)
    return query


# 查询函数的参数、返回值、返回码、参数示例
def stash_function_param_detail(public_function):
    function_param_list = TPublicFunctionParam.objects.filter(function_id=public_function.id)
    param_id_list = []
    return_id_list = []
    error_code_id_list = []
    for param in function_param_list:
        if param.type == FuncProcessCode.FUNCTION_PARAM_PARAM.value:
            param_id_list.append(param.param_id)
        elif param.type == FuncProcessCode.FUNCTION_PARAM_RETURN.value:
            return_id_list.append(param.param_id)
        else:
            error_code_id_list.append(param.code_id)
    # 查询当前页函数的参数和返回值具体内容
    error_code_list = TPublicErrorCode.objects.filter(id__in=error_code_id_list)
    # 转为字典
    item_param_list = []
    item_return_list = []
    item_error_code_list = []
    for param_id in param_id_list:
        param_data = TPublicParams.objects.filter(id=param_id).first()
        if not param_data:
            continue
        param_dict = param_data.object_to_dict()
        for param in function_param_list:
            if param.param_id == param_data.id and param.type == FuncProcessCode.FUNCTION_PARAM_PARAM.value:
                param_dict['example'] = param.example
                param_dict['required'] = param.required
        loop_index = 0
        param_dict = t_public_params.f_get_child_param(param_dict, loop_index)
        item_param_list.append(param_dict)
    for param_id in return_id_list:
        param_data = TPublicParams.objects.filter(id=param_id).first()
        if not param_data:
            continue
        return_param_dict = param_data.object_to_dict()
        loop_index = 0
        return_param_dict = t_public_params.f_get_child_param(return_param_dict, loop_index)
        item_return_list.append(return_param_dict)
    for error_code in error_code_list:
        item_error_code_list.append(error_code.object_to_dict())
    public_function.param_list = item_param_list
    public_function.return_list = item_return_list
    public_function.error_code_list = item_error_code_list


# 查询函数的参数
def stash_function_param(public_function):
    function_param_list = TPublicFunctionParam.objects.filter(function_id=public_function.id) \
        .filter(type=FuncProcessCode.FUNCTION_PARAM_PARAM.value)
    # 转为字典
    item_param_list = []
    for function_param_data in function_param_list:
        param_data = TPublicParams.objects.filter(id=function_param_data.param_id).first()
        param_dict = param_data.object_to_dict()
        item_param_list.append(param_dict)
    public_function.param_list = item_param_list


# 分页查询函数
def function_simple_list(request):
    condition = request.GET.get('condition', '').strip()
    page_size = request.GET.get('page_size')
    page_size = int(page_size)
    q = TPublicFunction.objects.filter(status__gte=FuncProcessCode.STATUS_RELEASE.value)
    if condition:
        q = q.filter(Q(function_name__contains=condition) | Q(function_desc__contains=condition))
    function_list = q.order_by('function_name')[:page_size]
    return function_list


# 新增函数封装
@csrf_exempt
def function_add_res(request):
    request_data = common.post_json_param(request)
    flag, res = function_add_unique(request_data)
    if not flag:
        return JsonResponse(res)
    first_name = common.get_first_name(request)
    function_add(request_data, first_name)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "新增成功!", "data": None}
    return JsonResponse(res)


# 编辑函数封装
@csrf_exempt
def function_update_res(request):
    request_data = common.post_json_param(request)
    flag, res = function_update_unique(request_data)
    if not flag:
        return JsonResponse(res)
    first_name = common.get_first_name(request)
    function_update(request_data,first_name)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "操作成功!", "data": None}
    return JsonResponse(res)


# 删除函数封装
@csrf_exempt
def function_del_res(request):
    request_data = common.post_json_param(request)
    function_id = request_data.get('id')
    # 删除前校验函数是否被功能引用
    function_count = TPublicCustomFunctionRelevance.objects.filter(function_id=function_id).count()
    if function_count > 0:
        res = {"code": ReturnEnum.ER_FAIL().code, "msg": "删除失败,该函数已被功能使用!", "data": None}
    else:
        # 待删除的函数
        public_function = TPublicFunction.objects.filter(id=function_id).first()
        function_name_en = public_function.function_name
        # 删除页面函数
        t_public_page_functions = t_public_page_function.objects.filter(function_name_en=function_name_en)
        if t_public_page_functions.exists():
            t_public_page_functions.delete()
        # 删除函数参数
        TPublicFunctionParam.objects.filter(function_id=function_id).delete()
        # 记录日志
        first_name = common.get_first_name(request)
        param_log = TPublicCustomFunctionLog(table_id=function_id, old_name=public_function.function_name,
                                             old_desc=public_function.function_desc, action_user=first_name,
                                             table_type=FuncProcessCode.LOG_FUNCTION.value,
                                             action_time=common.getNowTimeStamp(),
                                             action_type=FuncProcessCode.LOG_TYPE_DEL.value)
        param_log.save()
        # 删除函数
        public_function.delete()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "删除成功!", "data": None}
    return JsonResponse(res)


# 根据id查询函数封装
def function_get_by_id_res(request):
    return common.get_by_id_res(function_getById, request)


# 分页查询函数封装
def function_list_res(request):
    return common.page_res(function_page_list, request)


# 分页查询函数封装
def function_simple_list_res(request):
    return common.list_res(function_simple_list, request)


# 函数提交审核
def commit_function(request):
    # 需要展开的参数id
    param_id = request.GET.get('id')
    status = int(request.GET.get('status'))
    first_name = common.get_first_name(request)
    t_function = TPublicFunction.objects.filter(id=param_id).first()
    # 状态是已发布，或者提交人不是创建人，提示没有相关权限
    if (t_function.status == FuncProcessCode.STATUS_RELEASE.value or status == FuncProcessCode.STATUS_RELEASE.value) \
            or (t_function.author and t_function.author != first_name):
        res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg, "data": None}
    else:
        t_function.status = status
        t_function.save()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    return JsonResponse(res)


# 函数审核
def approve_function(request):
    # 需要展开的参数id
    param_id = request.GET.get('id')
    status = int(request.GET.get('status'))
    is_approve, first_name = common.approve_person(request)
    t_function = TPublicFunction.objects.filter(id=param_id).first()
    # 不是审核人，提示没有相关权限
    if not is_approve:
        res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg, "data": None}
    else:
        t_function.status = status
        # 撤销审核则将审核人和审核时间置为空
        if t_function.status == FuncProcessCode.STATUS_RELEASE.value and status == FuncProcessCode.STATUS_SUBMIT.value:
            t_function.release_time = None
            t_function.release_person = None
        else:
            t_function.release_time = common.getNowTimeStamp()
            t_function.release_person = first_name
        t_function.save()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    return JsonResponse(res)


# 函数发布
@csrf_exempt
def publish_function(request):
    # 需要展开的函数id
    function_id = request.GET.get('id')
    status = int(request.GET.get('status'))
    is_test, first_name = common.test_person(request)
    # 不是发布人，提示没有相关权限
    if not is_test or (status < FuncProcessCode.STATUS_RELEASE.value):
        res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg, "data": None}
    else:
        t_function = TPublicFunction.objects.filter(id=function_id).first()
        # 撤销发布则将发布人和发布时间置为空
        if t_function.status == FuncProcessCode.STATUS_PUBLISH.value and status == FuncProcessCode.STATUS_RELEASE.value:
            t_function.publish_time = None
            t_function.publish_person = None
            t_function.is_auto_test = FuncProcessCode.NO_AUTO_TEST.value
        else:
            t_function.publish_time = common.getNowTimeStamp()
            t_function.publish_person = first_name
        t_function.status = status
        t_function.save()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    return JsonResponse(res)


# 加入自动化测试
@csrf_exempt
def add_auto_test(request):
    # 需要展开的函数id
    function_id = request.GET.get('id')
    is_auto_test = int(request.GET.get('is_auto_test'))
    is_test, first_name = common.test_person(request)
    # 不是发布人，提示没有相关权限
    if not is_test:
        res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg, "data": dict()}
    else:
        t_function = TPublicFunction.objects.filter(id=function_id).first()
        t_function.is_auto_test = is_auto_test
        t_function.save()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": dict()}
    return JsonResponse(res)


@csrf_exempt
def vueFunction(request):
    result = PageFunction.create_vue_by_page_config('')
    if ReturnEnum.ER_SUCCESS().code == result['code']:
        rendered_string = result['data']['s_vue_component_content']
    else:
        rendered_string = ''
    return HttpResponse(rendered_string)