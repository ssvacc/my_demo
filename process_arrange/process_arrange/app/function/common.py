#    Copyright (c)  Fancyqube.com
#    @Author : niheng
#    @Date: 2023/3/14 下午5:10
#    @Description:
import errno
import json
import random
import traceback
import io
import uuid

from django.core.paginator import Paginator
from django.http import JsonResponse

from ConstEnum import FuncProcessName
from ReturnEnum import ReturnEnum
from datetime import datetime
import time


# 解析post请求的请求体body中的json数据
from app.table.other_app_table.t_sys_param import t_sys_param


def post_json_param(request):
    code0 = request.body.decode()
    code1 = code0.replace("'", "\'")
    request_data = json.loads(code1)
    return request_data

# 获取随机数
def get_random_Key():
    return random.uniform(0, 100)

# 获取当前时间戳
def now_time():
    return time.time()


# 获取当前时间秒
def getNowTime():
    now = datetime.today()
    return now.strftime("%Y%m%d%H%M%S")


# 获取当前时间秒
def getNowTimeStamp():
    timestamp = time.time()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))


# 获取姓名
def get_first_name(request):
    first_name = '盛荣凯'
    first_name = '徐国锋'
    first_name = '倪恒'
    first_name = '邢鑫'
    first_name = '王恒'
    first_name = '严旭'
    first_name = '丁俊'
    first_name = '陈硕'
    # first_name = request.user.first_name
    return first_name


# 是否审批人
def approve_person(request):
    flag = False
    first_name = get_first_name(request)
    approve_person_list = list(t_sys_param.objects.filter(Type=FuncProcessName.APPROVE_PERSON_TYPE.value).values_list('VDesc', flat=True))
    if first_name in approve_person_list:
        flag = True
    return flag, first_name


# 是否测试人员
def test_person(request):
    flag = False
    first_name = get_first_name(request)
    test_person_list = list(t_sys_param.objects.filter(Type=FuncProcessName.TEST_PERSON_TYPE.value).values_list('VDesc', flat=True))
    if first_name in test_person_list:
        flag = True
    return flag, first_name


# 是否参数提交人员
def is_submit_person(request):
    flag = False
    first_name = get_first_name(request)
    submit_person_list = list(t_sys_param.objects.filter(Type=FuncProcessName.SUBMIT_PERSON_TYPE.value).values_list('VDesc', flat=True))
    if first_name in submit_person_list:
        flag = True
    return flag, first_name


# 是否审批人
def f_is_approve_person(request):
    res = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": None}
    try:
        flag, first_name = approve_person(request)
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": flag}
    except Exception as e:
        traceback.print_exc()
    return JsonResponse(res)


# 分页查询中页码解析
def init_page(request):
    page_no = request.GET.get('page_no')
    page_size = request.GET.get('page_size')
    if page_no is None or page_size is None:
        return None, None
    page_no = int(page_no)
    page_size = int(page_size)
    if page_no <= 0 or page_size <= 0:
        return None, None
    return page_no, page_size


# 分页插件的返回值封装
def custom_paginator(data, page, page_size):
    if not data:
        page_info = {
            "current_page": 1,
            "total_page": 1,
            "has_next": False,
            "has_previous": False,
            "object_count": 0
        }
        return [], page_info
    if not page_size:
        page_size = 20
    p = Paginator(data, page_size)
    if int(page) <= p.num_pages:
        page_n = p.page(page)
        page_data = page_n.object_list
        page_info = {
            "current_page": page_n.number,
            "total_page": p.num_pages,
            "has_next": page_n.has_next(),
            "has_previous": page_n.has_previous(),
            "object_count": p.count
        }
    else:
        page_info = {
            "current_page": page,
            "total_page": p.num_pages,
            "has_next": False,
            "has_previous": False,
            "object_count": p.count
        }
        page_data = []
    return page_data, page_info


# 根据id查询并返回结果
def get_by_id_res(function, request):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": None}
    result = function(request)
    res["data"] = result.object_to_dict()
    return JsonResponse(res)


# 查询列表并返回结果
def list_res(function, request):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": None}
    result_list = function(request)
    dict_list = []
    for result in result_list:
        dict_data = result.object_to_dict()
        dict_list.append(dict_data)
    res["data"] = dict_list
    return JsonResponse(res)


# 分页查询并返回结果
def page_res(function, request):
    page_no, page_size = init_page(request)
    if page_no is None or page_size is None:
        res = {'code': ReturnEnum.ER_PARAMENTER().code, 'msg': ReturnEnum.ER_PARAMENTER().msg, 'data': None}
        return JsonResponse(res)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
    page = function(request, page_no, page_size)
    if page['total'] == 0:
        res["data"] = page
        return JsonResponse(res)
    dict_list = []
    for result in page['data']:
        dict_data = result.object_to_dict()
        dict_list.append(dict_data)
    res["data"] = {'total': page['total'], 'data': dict_list}
    return JsonResponse(res)


# 新增数据并返回结果
def add_res(check_function, function, request):
    request_data = post_json_param(request)
    if check_function is not None:
        flag, res = check_function(request_data)
        if not flag:
            return JsonResponse(res)
    first_name = get_first_name(request)
    function(request_data, first_name)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "新增成功!", "data": None}
    return JsonResponse(res)


# 修改数据并返回结果
def update_res(function, request):
    request_data = post_json_param(request)
    first_name = get_first_name(request)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": None}
    function(request_data, first_name)
    res["msg"] = "操作成功!"
    return JsonResponse(res)


# 删除数据并返回结果
def del_res(function, request):
    request_data = post_json_param(request)
    first_name = get_first_name(request)
    msg = function(request_data, first_name)
    if msg is None:
        res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "删除成功!", "data": None}
    else:
        res = {"code": ReturnEnum.ER_FAIL().code, "msg": "删除失败," + msg, "data": None}
    return JsonResponse(res)


# 接口函数返回值预处理，不能转json的数据转为地址值字符串
def deal_dict_json(result, loop_index):
    loop_index += 1
    # 设置递归层数，超过5次不再递归
    if loop_index > 5:
        return
    for key, value in result.items():
        if type(value) is dict:
            deal_dict_json(value, loop_index)
        if type(value) == type(lambda: None):
            result[key] = str(value)
        if isinstance(value, (io.IOBase, io.RawIOBase)):
            result[key] = str(value)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5 (except OSError, exc: for Python <2.5)
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise