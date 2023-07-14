# -*- coding: utf-8 -*-
import json
import random

from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ConstEnum import FuncProcessCode, FuncProcessName, PUBLIC_CONFIG_INFO
from ReturnEnum import ReturnEnum
from app.function import common, approve_comments
from app.table.t_public_custom_function_log_model import t_public_custom_function_log as TPublicCustomFunctionLog
from app.table.t_public_function_param_model import t_public_function_param as TPublicFunctionParam
from app.table.t_public_params_field_model import t_public_params_field
from app.table.t_public_params_model import t_public_params as TPublicParams
from app.table.t_public_custom_function_param_model import t_public_custom_function_param as TPublicCustomParam


# 新增参数唯一校验
def param_add_unique(request_data):
    count = TPublicParams.objects.filter(param_name=request_data.get('param_name')).count()
    res = ReturnEnum.ER_SUCCESS()
    if count > 0:
        res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
               'msg': request_data.get('param_name') + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg}
    return count == 0, res


# 编辑参数唯一校验
def param_update_unique(request_data):
    param_id = request_data.get('id')
    param_name = request_data.get('param_name')
    count = TPublicParams.objects.filter(Q(param_name=param_name) & ~Q(id=param_id)).count()
    res = ReturnEnum.ER_SUCCESS()
    if count > 0:
        res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
               'msg': param_name + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg}
    return count == 0, res

# 新增参数
def param_add(request_data, first_name):
    params = TPublicParams(param_name=request_data.get('param_name'),
                           param_detail=request_data.get('param_detail'),
                           param_desc=request_data.get('param_desc'),
                           status=FuncProcessCode.STATUS_NO_ACTIVATE.value,
                           data_type=request_data.get('data_type'))
    child_id = request_data.get('child_id')
    if child_id is not None:
        params.child_id = child_id
    select_info_id = request_data.get('select_info_id')
    if select_info_id:
        params.select_info_id = select_info_id
    params.create_person = first_name
    params.create_time = common.getNowTimeStamp()
    params.apply_time = PUBLIC_CONFIG_INFO.DEFAULT_EMPTY_DATE_TIME.value
    params.save()
    # 记录日志
    param_log = TPublicCustomFunctionLog(table_id=params.id, action_user=first_name,
                                         table_type=FuncProcessCode.LOG_PARAM.value,
                                         action_type=FuncProcessCode.LOG_TYPE_ADD.value,
                                         new_name=request_data.get('param_name'),
                                         new_desc=request_data.get('param_desc'),
                                         action_time=common.getNowTimeStamp())
    param_log.save()

    # type=22
    data_type=request_data.get('data_type')
    if data_type==FuncProcessCode.FIELD_DATA_TYPE.value:
        selectedValues = request_data.get('selectedValues')
        for row in selectedValues:
            param_name=request_data.get('param_name')
            param_desc=request_data.get('param_desc')
            params_value = TPublicParams.objects.filter(param_name=param_name).first()
            param_id = params_value.id
            field_param_id = int(row['field_param_id'])
            field_param_name = row['field_param_name']
            field_value = row['field_value']
            t_public_params_field.objects.create(param_id=param_id, param_name=param_name,
                                                 param_desc=param_desc,field_param_id=field_param_id,
                                                 field_param_name=field_param_name,field_value=field_value)  

# 编辑参数
def param_update(request_data, first_name):
    params_id = request_data.get('id')
    params = TPublicParams.objects.get(id=params_id)
    new_name = request_data.get('param_name')
    if params.status == FuncProcessCode.STATUS_NO_ACTIVATE.value:
        params.param_name = new_name
        if request_data.get('data_type'):
            params.data_type = request_data.get('data_type')
        if request_data.get('child_id'):
            params.child_id = request_data.get('child_id')
        if request_data.get('select_info_id'):
            params.select_info_id = request_data.get('select_info_id')
    old_param = params.param_name
    old_desc = params.param_desc
    params.param_desc = request_data.get('param_desc')
    params.param_detail = request_data.get('param_detail')
    params.save()
    custom_param_list = TPublicCustomParam.objects.filter(param_id=params_id)
    if len(custom_param_list) > 0:
        for custom_param in custom_param_list:
            custom_param.param_name = new_name
            custom_param.param_desc = request_data.get('param_desc')
        TPublicCustomParam.objects.bulk_update(custom_param_list, ["param_desc"])
    # 记录日志
    param_log = TPublicCustomFunctionLog(table_id=params_id, old_name=old_param, old_desc=old_desc,
                                         action_user=first_name,
                                         new_name=new_name,
                                         new_desc=request_data.get('param_desc'),
                                         action_time=common.getNowTimeStamp(),
                                         table_type=FuncProcessCode.LOG_PARAM.value,
                                         action_type=FuncProcessCode.LOG_TYPE_UPDATE.value)
    param_log.save()

    # type=22  Field类型参数编辑
    data_type=request_data.get('data_type')
    if data_type==FuncProcessCode.FIELD_DATA_TYPE.value:
        param_field = t_public_params_field.objects.filter(param_id=params_id)
        param_field.delete()
        selectedValues = request_data.get('selectedValues')
        for row in selectedValues:
            param_name=request_data.get('param_name')
            param_desc=request_data.get('param_desc')
            params_value = TPublicParams.objects.filter(param_name=param_name).first()
            param_id = params_value.id
            field_param_id = int(row['field_param_id'])
            field_param_name = row['field_param_name']
            field_value = row['field_value']
            t_public_params_field.objects.create(param_id=param_id, param_name=param_name,
                                                 param_desc=param_desc,field_param_id=field_param_id,
                                                 field_param_name=field_param_name,field_value=field_value) 


# 根据id查询参数
def param_getByIdList(request):
    param_id_list = request.GET.get('param_id_list')
    param_id_list = param_id_list.split(',')
    return TPublicParams.objects.filter(id__in=param_id_list)


# 根据id查询参数
def param_getByName(request):
    params_name = request.GET.get('param_name')
    return TPublicParams.objects.filter(param_name__icontains=params_name).order_by('-id')


# 下拉框查询参数
def param_list(request):
    condition = request.GET.get('condition', '').strip()
    page_size = request.GET.get('page_size')
    release = request.GET.get('release')
    page_size = int(page_size)
    q = TPublicParams.objects
    if release:
        q = q.filter(status=FuncProcessCode.STATUS_RELEASE.value)
    if condition:
        q = q.filter(Q(param_name__icontains=condition) | Q(param_desc__contains=condition)
                     | Q(param_detail__contains=condition))
    else:
        q = q.filter()
    return q.order_by('param_name')[:page_size]


# 新增参数封装
@csrf_exempt
def param_add_res(request):
    request_data = common.post_json_param(request)
    flag, res = param_add_unique(request_data)
    if not flag:
        return JsonResponse(res)
    first_name = common.get_first_name(request)
    param_add(request_data, first_name)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "新增成功!", "data": None}
    return JsonResponse(res)


# 编辑参数封装
@csrf_exempt
def param_update_res(request):
    request_data = common.post_json_param(request)
    flag, res = param_update_unique(request_data)
    if not flag:
        return JsonResponse(res)
    first_name = common.get_first_name(request)
    param_update(request_data, first_name)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "操作成功!", "data": None}
    return JsonResponse(res)


# 删除参数封装
@csrf_exempt
def param_del_res(request):
    request_data = common.post_json_param(request)
    first_name = common.get_first_name(request)
    param_id = request_data.get('id')
    res = check_param_used(param_id)
    if res['code'] == ReturnEnum.ER_SUCCESS().code:
        t_public_param = TPublicParams.objects.filter(id=param_id).first()
        data_type = t_public_param.data_type
        if data_type==FuncProcessCode.FIELD_DATA_TYPE.value:
            param_field = t_public_params_field.objects.filter(param_id=param_id)
            param_field.delete()
        # 记录日志
        param_log = TPublicCustomFunctionLog(table_id=param_id, old_name=t_public_param.param_name,
                                             old_desc=t_public_param.param_desc, action_user=first_name,
                                             action_time=common.getNowTimeStamp(),
                                             table_type=FuncProcessCode.LOG_PARAM.value,
                                             action_type=FuncProcessCode.LOG_TYPE_DEL.value)
        param_log.save()
        t_public_param.delete()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "删除成功!", "data": None}
    return JsonResponse(res)


# 校验参数是否被引用
def check_param_used(param_id):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    # 校验参数是否被其他参数作为子集
    parent_flag = False
    param_parent_list = TPublicParams.objects.filter(child_id__contains=param_id)
    param_id_str = str(param_id)
    for param_parent in param_parent_list:
        child_id_str = param_parent.child_id
        child_id = child_id_str.split(',')
        for child in child_id:
            if param_id_str == child:
                parent_flag = True
                break
    if parent_flag:
        res = {"code": ReturnEnum.ER_FAIL().code, "msg": "删除失败,该参数已被其他参数引用", "data": None}
    else:
        # 校验参数是否被其他函数引用
        params_count = TPublicFunctionParam.objects.filter(param_id=param_id).count()
        if params_count > 0:
            res = {"code": ReturnEnum.ER_FAIL().code, "msg": "删除失败,该参数已被函数使用", "data": None}
    return res


# params = Params.objects.all()[page_no:page_size]
# 分页查询参数
def param_page_list(request, page_no, page_size):
    condition = request.GET.get('condition', '').strip()
    if condition is not None:
        params_list = TPublicParams.objects.filter(Q(param_name__contains=condition) | Q(param_desc__contains=condition)
                                                   | Q(param_detail__contains=condition)).order_by('param_name')
    else:
        params_list = TPublicParams.objects.filter().order_by('param_name')
    page_data, page_info = common.custom_paginator(params_list, page_no, page_size)
    page = {'total': page_info['object_count'], 'data': page_data}
    return page


@csrf_exempt
def param_page_res(request):
    return common.page_res(param_page_list, request)


# 分页查询参数，带所有子集参数
@csrf_exempt
def param_child_page_res(request):
    page_no, page_size = common.init_page(request)
    if page_no is None or page_size is None:
        res = {'code': ReturnEnum.ER_PARAMENTER().code, 'msg': ReturnEnum.ER_PARAMENTER().msg, 'data': None}
        return JsonResponse(res)
    condition = request.GET.get('condition', '').strip()
    query = TPublicParams.objects
    status = request.GET.get('status')
    if status:
        query = query.filter(status=status)
    if condition == FuncProcessCode.COMMENT_NO_READ_DESC.value:
        param_id_list = approve_comments.get_no_comment_list(FuncProcessName.PUBLIC_PARAM_CN.value, common.get_first_name(request))
        query = query.filter(id__in=param_id_list)
    elif condition:
        # 字段模糊匹配，创建人，审核人精准匹配
        query = query.filter(Q(create_person=condition)| Q(apply_person=condition)| Q(release_person=condition)
                             | Q(param_name__icontains=condition) | Q(param_desc__icontains=condition)
                             | Q(param_detail__icontains=condition))
    params_list = query.order_by('-release_time', '-id')
    page_data, page_info = common.custom_paginator(params_list, page_no, page_size)
    dict_list = []
    for param in page_data:
        dict_data = param.object_to_dict()
        loop_index = 0
        dict_data = f_get_child_param(dict_data, loop_index)
        dict_data['key'] = get_random_Key()
        dict_list.append(dict_data)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    res["data"] = {'total': page_info['object_count'], 'data': dict_list}
    return JsonResponse(res)


def f_get_child_param(dict_data, loop_index):
    loop_index += 1
    # 递归深度限制
    if loop_index >= 5:
        return dict_data
    if dict_data['child_id']:
        if dict_data['data_type'] == FuncProcessCode.DICT_DATA_TYPE.value:
            child_dict_list = []
            for c_id in dict_data['child_id'].split(','):
                t_param = TPublicParams.objects.filter(id=c_id).first()
                child_param_dict = t_param.object_to_dict()
                child_param_dict = f_get_child_param(child_param_dict, loop_index)
                child_param_dict['key'] = get_random_Key()
                child_dict_list.append(child_param_dict)
            dict_data['child_list'] = child_dict_list
        
        elif dict_data['data_type']==FuncProcessCode.FIELD_DATA_TYPE.value:
            # Field类型
            child_dict_list = []
            field_list = []
            for c_id in dict_data['child_id'].split(','):
                t_param = TPublicParams.objects.filter(id=c_id).first()
                child_param_dict = t_param.object_to_dict()
                child_param_dict = f_get_child_param(child_param_dict, loop_index)
                child_param_dict['key'] = get_random_Key()
                child_dict_list.append(child_param_dict)
            dict_data['child_list'] = child_dict_list
            # 返回Field_value
            param_name = dict_data['param_name']
            field_param_list = t_public_params_field.objects.filter(param_name=param_name).values()
            if field_param_list.exists():
                for row in field_param_list:
                    field_param_id=row['field_param_id']
                    field_param_name=row['field_param_name']
                    field_value = eval(row['field_value'])
                    field_list.append({"field_param_id":field_param_id,"field_param_name":field_param_name,"field_value":field_value})
                dict_data['field_list'] = field_list

        elif dict_data['data_type'] == FuncProcessCode.LIST_DATA_TYPE.value:
            t_param = TPublicParams.objects.filter(id=dict_data['child_id']).first()
            child_param_dict = t_param.object_to_dict()
            child_param_dict = f_get_child_param(child_param_dict, loop_index)
            child_param_dict['key'] = get_random_Key()
            dict_data['child_list'] = child_param_dict
        else:
            dict_data['child_list'] = []
    return dict_data


# table树形控件懒加载时，查询子参数
@csrf_exempt
def f_query_child_param(request):
    # 需要展开的参数id
    child_id = request.GET.get('child_id')
    data_type = int(request.GET.get('data_type'))
    child_dict_list = []
    if data_type == FuncProcessCode.DICT_DATA_TYPE.value:
        for c_id in child_id.split(','):
            query_child_param(child_dict_list, c_id)
    elif data_type == FuncProcessCode.LIST_DATA_TYPE.value:
        query_child_param(child_dict_list, child_id)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": child_dict_list}
    return JsonResponse(res)


def query_child_param(child_dict_list, child_id):
    t_param = TPublicParams.objects.filter(id=child_id).first()
    child_param_dict = t_param.object_to_dict()
    # 列表类型需往下查一层，用于页面展示数据类型
    if child_param_dict['child_id'] and child_param_dict['data_type'] == FuncProcessCode.LIST_DATA_TYPE.value:
        t_param_son = TPublicParams.objects.filter(id=t_param.child_id).first()
        child_param_son = t_param_son.object_to_dict()
        child_param_son['key'] = get_random_Key()
        child_param_dict['child_list'] = child_param_son
    child_param_dict['key'] = get_random_Key()
    child_dict_list.append(child_param_dict)


# 获取随机数
def get_random_Key():
    return random.uniform(0, 100)


# 不分页查询参数封装
@csrf_exempt
def param_list_res(request):
    return common.list_res(param_list, request)


# 根据参数名不分页查询参数封装
@csrf_exempt
def param_list_by_name_res(request):
    return common.list_res(param_getByName, request)


# 根据参数idList查询参数封装
@csrf_exempt
def param_by_id_list_res(request):
    return common.list_res(param_getByIdList, request)


# 批量删除接口，todo 演示用，不上online
@csrf_exempt
def del_by_id_list_res(request):
    first_name = common.get_first_name(request)
    request_data = common.post_json_param(request)
    id_list = request_data.get('id_list')
    for param_id in id_list:
        res = check_param_used(param_id)
        if res['code'] != ReturnEnum.ER_SUCCESS().code:
            return JsonResponse(res)
    for param_id in id_list:
        t_public_param = TPublicParams.objects.filter(id=param_id).first()
        # 记录日志
        param_log = TPublicCustomFunctionLog(table_id=param_id, old_name=t_public_param.param_name,
                                             old_desc=t_public_param.param_desc, action_user=first_name,
                                             action_time=common.getNowTimeStamp(),
                                             table_type=FuncProcessCode.LOG_PARAM.value,
                                             action_type=FuncProcessCode.LOG_TYPE_DEL.value)
        param_log.save()
        t_public_param.delete()
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "批量删除成功!", "data": None}
    return JsonResponse(res)


# 参数提交审核
def commit_param(request):
    # 需要展开的参数id
    param_id = request.GET.get('id')
    status = int(request.GET.get('status'))
    is_submit_person, first_name = common.is_submit_person(request)
    t_param = TPublicParams.objects.filter(id=param_id).first()
    # 已审核的参数不能调用提交接口
    if t_param.status == FuncProcessCode.STATUS_RELEASE.value and status == FuncProcessCode.STATUS_RELEASE.value:
        check_flag = False
    # 提交人和创建人自己可以提交审核
    elif is_submit_person or t_param.create_person and t_param.create_person == first_name:
        check_flag = True
    else:
        check_flag = False
    if check_flag:
        if status == FuncProcessCode.STATUS_SUBMIT.value:
            t_param.apply_person = first_name
            t_param.apply_time = common.getNowTimeStamp()
            t_param.release_person = ''
            t_param.release_time = PUBLIC_CONFIG_INFO.DEFAULT_EMPTY_DATE_TIME.value
        if status == FuncProcessCode.STATUS_NO_ACTIVATE.value:
            t_param.apply_person = ''
            t_param.apply_time = PUBLIC_CONFIG_INFO.DEFAULT_EMPTY_DATE_TIME.value
        t_param.status = status
        t_param.save()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    else:
        res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg, "data": None}
    return JsonResponse(res)


# 参数审核
def approve_param(request):
    # 需要展开的参数id
    param_id = request.GET.get('id')
    status = int(request.GET.get('status'))
    is_approve, first_name = common.approve_person(request)
    t_param = TPublicParams.objects.filter(id=param_id).first()
    # 不是审核人，提示没有相关权限
    if not is_approve:
        res = {"code": ReturnEnum.ER_NO_ROLE().code, "msg": ReturnEnum.ER_NO_ROLE().msg, "data": None}
    else:
        # 撤销审核则将审核人和审核时间置为空
        if t_param.status == FuncProcessCode.STATUS_RELEASE.value and status == FuncProcessCode.STATUS_SUBMIT.value:
            t_param.release_person = ''
            t_param.release_time = PUBLIC_CONFIG_INFO.DEFAULT_EMPTY_DATE_TIME.value
        else:
            t_param.release_person = first_name
            t_param.release_time = common.getNowTimeStamp()
        t_param.status = status
        t_param.save()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    return JsonResponse(res)
