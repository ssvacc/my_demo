#    Copyright (c)  Fancyqube.com
#    @Author : ni heng
#    @Date: 2023/3/14 下午5:10
#    @Description:
# -*- coding: utf-8 -*-
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction

from ConstEnum import FuncProcessCode, FuncProcessName, PUBLIC_CONFIG_INFO
from ReturnEnum import ReturnEnum
from app.function import common, approve_comments
from app.function.common import get_random_Key, post_json_param
from app.table.t_public_custom_function_log_model import t_public_custom_function_log \
    as TPublicCustomFunctionLog
from app.table.t_public_function_model import t_public_function
from app.table.t_public_function_param_model import t_public_function_param as TPublicFunctionParam
from app.table.t_public_page_function_model import t_public_page_function
from app.table.t_public_page_model import t_public_page
from app.table.t_public_params_model import t_public_params as TPublicParams
from app.table.t_public_custom_function_param_model import t_public_custom_function_param \
    as TPublicCustomParam

from app.table.t_public_function_param_model import t_public_function_param

# from app.common_function.sqlalchemy_sesssion import DBHelper
# from app.models.hq_db.t_public_params import TPublicParam
# from app.table.t_public_class_model import t_public_class as TPublicClass


# 新增参数唯一校验
def param_add_unique(request_data):
    param_name = request_data.get('param_name','').strip()
    count = TPublicParams.objects.filter(param_name=param_name).count()
    res = ReturnEnum.ER_SUCCESS()
    if count > 0:
        res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
               'msg': param_name + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg}
    return count == 0, res


# 编辑参数唯一校验
def param_update_unique(request_data):
    param_id = request_data.get('id')
    param_name = request_data.get('param_name', '').strip()
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
    params.release_time = PUBLIC_CONFIG_INFO.DEFAULT_EMPTY_DATE_TIME.value
    params.save()
    # 记录日志
    param_log = TPublicCustomFunctionLog(table_id=params.id, action_user=first_name,
                                         table_type=FuncProcessCode.LOG_PARAM.value,
                                         action_type=FuncProcessCode.LOG_TYPE_ADD.value,
                                         new_name=request_data.get('param_name'),
                                         new_desc=request_data.get('param_desc'),
                                         action_time=common.getNowTimeStamp())
    param_log.save()


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
        q = q.filter(Q(param_name__icontains=condition) | Q(param_desc__icontains=condition)
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
        # 记录日志
        param_log = TPublicCustomFunctionLog(table_id=param_id, old_name=t_public_param.param_name,
                                             old_desc=t_public_param.param_desc,
                                             action_user=first_name,
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
        query = query.filter(Q(create_person=condition) | Q(apply_person=condition)| Q(release_person=condition)
                             | Q(param_name__icontains=condition) | Q(param_desc__icontains=condition)
                             | Q(param_detail__icontains=condition))
    params_list = query.order_by('-release_time', '-id')
    page_data, page_info = common.custom_paginator(params_list, page_no, page_size)
    dict_list = []
    for param in page_data:
        dict_data = param.object_to_dict()
        loop_index = 0
        dict_data = f_get_child_param(dict_data, loop_index, False)
        dict_data['key'] = get_random_Key()
        dict_list.append(dict_data)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    res["data"] = {'total': page_info['object_count'], 'data': dict_list}
    return JsonResponse(res)

# show_enum True展开显示枚举值内容
def f_get_child_param(dict_data, loop_index, show_enum):
    loop_index += 1
    # 递归深度限制
    if loop_index >= FuncProcessCode.MAX_LOOP_INDEX.value:
        return dict_data
    if dict_data['data_type'] == FuncProcessCode.ENUM_DATA_TYPE.value and show_enum:
        res_data_list =  common.query_enum_by_select_id(dict_data['select_info_id'])
        dict_data['child_list'] = res_data_list
        return dict_data
    if dict_data['child_id']:
        if dict_data['data_type'] == FuncProcessCode.DICT_DATA_TYPE.value:
            child_dict_list = []
            for c_id in dict_data['child_id'].split(','):
                t_param = TPublicParams.objects.filter(id=c_id).first()
                child_param_dict = t_param.object_to_dict()
                child_param_dict = f_get_child_param(child_param_dict, loop_index, show_enum)
                child_param_dict['key'] = get_random_Key()
                child_dict_list.append(child_param_dict)
            dict_data['child_list'] = child_dict_list
        elif dict_data['data_type'] == FuncProcessCode.LIST_DATA_TYPE.value:
            t_param = TPublicParams.objects.filter(id=dict_data['child_id']).first()
            child_param_dict = t_param.object_to_dict()
            child_param_dict = f_get_child_param(child_param_dict, loop_index, show_enum)
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


# 参数提交审核
@csrf_exempt
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
@csrf_exempt
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
            t_param.release_time = common.getNowTimeStamp()
            t_param.release_person = first_name
        t_param.status = status
        t_param.save()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    return JsonResponse(res)



#查询页面列表
@csrf_exempt
def page_list_res(request):
    page_queryset = t_public_page_function.objects.values('page_name_en', 'page_name_cn', 'function_name_en', 'function_name_cn')
    page_dict = {}
    for page_data in page_queryset:
        page_name_en = page_data['page_name_en']
        page_name_cn = page_data['page_name_cn']
        function_name_en = page_data['function_name_en']
        function_name_cn = page_data['function_name_cn']
        if page_name_en not in page_dict:
            page_dict[page_name_en] = {
                'page_name_en': page_name_en,
                'page_name_cn': page_name_cn,
                'function_name': [],
            }
        
        page_dict[page_name_en]['function_name'].append({'function_name_en':function_name_en, 'function_name_cn':function_name_cn})

    page_list = list(page_dict.values())
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": page_list}
    return JsonResponse(res)




#查询参数类型
@csrf_exempt
def params_list_res(request):
    param_queryset = TPublicParams.objects.filter(data_type=21).values('param_name', 'param_desc')
    param_list = []
    for param_data in param_queryset:
        param_name = param_data['param_name']
        param_desc = param_data['param_desc']
        name = f"{param_name}:{param_desc}"
        param_list.append({
            'param_name': param_name,
            'param_desc': param_desc,
            'name': name,
        })
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": param_list}
    return JsonResponse(res)



from django.http import JsonResponse
@csrf_exempt
def add_page_list(request):
    # 创建页面  生成 页面名  类名  函数名
    request_data = post_json_param(request)
    param_name = request_data.get('param_name', '').strip()
    page_name_en, page_name_cn = param_name.split(':')
    flag = page_only(page_name_en) #判断是否重复添加
    if not flag:
        page_add(page_name_cn, page_name_en) #创建页面数据
        # first_name = request_data.get('first_name', '').strip()  #创建人
        first_name = common.get_first_name(request)
        #创建page函数
        function_name_list = ['menu','search','button','data','style']
        function_desc_list = ['菜单区','搜索区','按钮区','数据区','样式区']
        for i in range(len(function_name_list)):
            function_name_en = page_name_en + '::'+ function_name_list[i]
            function_name_cn = page_name_cn + '::'+ function_desc_list[i]
            function_data = {
                'function_name_en': function_name_en,
                'function_name_cn': function_name_cn,
                'page_name_en': page_name_en,
                'page_name_cn': page_name_cn,
                'first_name':first_name,
            }
            page_function_add(function_data)
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "新增成功!", "data": None}
    else:
        res = {"code": ReturnEnum.ER_FAIL().code, "msg": "页面不可重复添加!", "data": None}
    return JsonResponse(res)

def page_only(param_name_en):
    return t_public_page.objects.filter(page_name_en=param_name_en).exists()
    #判断页面是否创建


def page_add(page_name_cn, page_name_en):
    #新增页面
    create_time = common.getNowTimeStamp()
    t_public_page.objects.create(page_name_cn=page_name_cn, page_name_en=page_name_en,create_time=create_time)


# 新增page函数
def page_function_add(request_data):
    page_name_en = request_data.get('page_name_en', '').strip()
    page_name_cn = request_data.get('page_name_cn', '').strip()
    function_name_en = request_data.get('function_name_en', '').strip()
    function_name_cn = request_data.get('function_name_cn', '').strip()
    status=FuncProcessCode.STATUS_NO_ACTIVATE.value
    is_auto_test=FuncProcessCode.NO_AUTO_TEST.value
    url = FuncProcessCode.SVN_BASE_URL.value
    create_time = common.getNowTimeStamp()

    function_detail=function_name_cn
    class_name = page_name_en
    first_name = request_data.get('first_name','').strip()
    # first_name = common.get_first_name(request)

    with transaction.atomic():
        t_public_page_function.objects.create(
            page_name_en=page_name_en,
            page_name_cn=page_name_cn,
            function_name_en=function_name_en,
            function_name_cn=function_name_cn
        )
        t_public_function.objects.create(
            status=status,
            is_auto_test=is_auto_test,
            function_name=function_name_en,
            function_desc=function_name_cn,
            function_detail=function_detail,
            class_name=class_name,
            author=first_name,
            s_principal = first_name,
            url =url,
            create_time = create_time
        )
        function_param = t_public_function.objects.filter(function_name=function_name_en).first()
        function_id = function_param.id
        TPublicFunctionParam.objects.create(function_id=function_id,type=0,code_id=1)
        TPublicFunctionParam.objects.create(function_id=function_id,type=0,code_id=2)

#删除页面及相关数据
@csrf_exempt
def del_page_list(request):
    res = {"code": ReturnEnum.ER_FAIL().code, "msg": "删除失败!", "data": None}
    """
    删除表：1、t_public_page   page_name_en    4
            2、t_public_function  function_name--function_name_en  3
            3、t_public_page_function   function_name_en   1
            4、t_public_function_param   function_id--t_public_function.id--function_name  2
    """
    try:
        request_data = post_json_param((request))
        page_name_en = request_data.get('page_name_en')
        function_name_list = request_data.get('function_name')  # 页面函数列表
        for row in range(len(function_name_list)):
            function_name_en = function_name_list[row]["function_name_en"]
            t_public_page_function.objects.filter(function_name_en=function_name_en).delete()
            public_function = t_public_function.objects.filter(function_name=function_name_en).first()
            function_id = public_function.id
            t_public_function_param.objects.filter(function_id=function_id).delete()
            public_function.delete()
        t_public_page.objects.filter(page_name_en=page_name_en).first().delete()
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "删除成功!", "data": None}
    except Exception as ex:
        res = {"code": ReturnEnum.ER_FAIL().code, "msg": "删除失败!", "data": str(ex)}
    return JsonResponse(res)


@csrf_exempt
# 预览界面
def page_button_show(request):
    request_data = post_json_param(request)
    function_name_en = request_data.get('function_name_en')
    public_function_values = t_public_function.objects.filter(function_name=function_name_en).first()
    function_id = public_function_values.id
    t_params_query = TPublicFunctionParam.objects.filter(id=function_id,type=1).values()
    for query in t_params_query:
        query
    pass
        






    





    




