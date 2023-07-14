import functools

from ReturnEnum import ReturnEnum


# 演示函数


import importlib
from django.db.models import Model

from app.common_function.zhuangshiqi import FuncCacheWrapper1
from app.function.interfaceFunctionCheck import InterfaceFunctionCheck


def get_function(func_name, func_route, request=None, model_info=None):
    if func_name.find("::") >= 0:
        class_name = func_name.split('::')[0].replace("()", "").strip()
        func_name = func_name.split('::')[-1].replace("()", "").strip()
    else:
        class_name = ""
        func_name = func_name.replace("()", "").strip()
    if class_name:
        admin_class = getattr(importlib.import_module(func_route), class_name)
        if request:
            admin_class.request = request
        if model_info:
            if isinstance(model_info, Model):
                model_class = model_info
            else:
                model_file_route = model_info.split('+')[0]
                model_class_name = model_info.split('+')[-1]
                model_class = getattr(importlib.import_module(model_file_route), model_class_name)
            admin_class.model = model_class
        func_obj = getattr(admin_class(), func_name)
    else:
        module = importlib.import_module(func_route)
        func_obj = getattr(module, func_name)
    return func_obj


def show_add(English_score, math_score, **kwargs):
    num1 = int(English_score)
    num2 = int(math_score)
    sum_score = num1 + num2
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": dict()}
    res['data']['sum_score'] = sum_score
    return res


# 演示函数
def show_sub_value(English_score, math_score, **kwargs):
    num1 = int(English_score)
    num2 = int(math_score)
    sub_score = num1 - num2
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": dict()}
    res['data']['number'] = sub_score
    return res


# 演示函数
def show_division(English_score, math_score, **kwargs):
    num1 = int(English_score)
    num2 = int(math_score)
    sum_score = num1.divide(num2)
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": dict()}
    res['data']['number'] = sum_score
    return res





# 演示函数,获取数组中的最大值
def get_max_number_value(test_param_list, **kwargs):
    max_value = 0
    for num in test_param_list:
        num = int(num)
        if num > max_value:
            max_value = num
    return max_value


# 演示函数,获取数组中的最大值
def get_max_number_data(**kwargs):
    test_param_list = kwargs.get("test_param_list")
    max_value = 0
    for num in test_param_list:
        num = int(num)
        if num > max_value:
            max_value = num
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": dict()}
    res['data']['max_value'] = max_value
    return res


# 演示函数,获取数组中的最大值
def get_max_number_param_err(param_list, **kwargs):
    # 返回值
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": dict()}
    res['data']['max_value'] = get_max_number_res_err(param_list)
    return res


# 演示函数,获取数组中的最大值
def get_max_number_res_err(test_param_list, **kwargs):
    max_value = 0
    for num in test_param_list:
        num = int(num)
        if num > max_value:
            max_value = num
    return max_value


# 演示函数,获取数组中的最大值(最小功能函数)
def get_max_number(number_list, **kwargs):
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": dict()}
    max_value = 0
    for num in number_list:
        num = int(num)
        if num > max_value:
            max_value = num
    res['data']['max_value'] = max_value
    return res


# 演示函数,筛选所有奇数或者偶数
def show_number_odd_even_detail(number_list, odd_number, **kwargs):
    result_list = []
    for num in number_list:
        num = int(num)
        is_odd = num % 2 != 0
        if is_odd == odd_number:
            result_list.append(num)
    return result_list


# 演示函数,获取数组中的最大值(最小功能函数)
def show_number_odd_even(is_odd, number_list, **kwargs):
    # 返回值
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "Success!", "data": dict()}
    res['data']['number_list'] = show_number_odd_even_detail(number_list, is_odd)
    return res


def fir(func2):
    print('3')
    @functools.wraps(func2)
    def warp2(*args,**kwargs):
        print('4')
        func2(*args,**kwargs)
        print('10')
    return warp2
def sec(func1):
    print('1')
    @secOut
    @functools.wraps(func1)
    def warp1(*args,**kwargs):
        print('6')
        func1(*args,**kwargs)
        print('8')
    return warp1
def secOut(func3):
    print('2')
    @functools.wraps(func3)
    def warpA(*args, **kwargs):
        print('5')
        func3(*args, **kwargs)
        print('9')
    return warpA
# @fir
# @sec
@FuncCacheWrapper1
@InterfaceFunctionCheck
def aa(c,d, **kwargs):
    print(c)
    print(d)
# 先执行离函数最近的装饰器（从上而下进栈，先出栈的先执行,如果遇到装饰器内函数，则先暂停，执行完非装饰器函数的代码再执行）


if __name__ == '__main__':
    dicts = dict(c='c', d='d', e='e')
    func_obj = get_function('aa', 'app.custom_function.math')
    func_obj(**dicts)
    # a = func_obj.__code__.co_varnames
    # print(a)
    # print('num')
    # print(num)