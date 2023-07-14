from django.http import JsonResponse
import pymysql
import datetime

from ReturnEnum import ReturnEnum
from app import models

# 存放所有的参数 params：dict格式
def params_list(params_level_list):
    for level in params_level_list:
        a = params_level_list()
    return None


# 存放所有的返回值 result：dict格式
def result_list(result_list):
    return None


# 根据参数层级组装函数
def run_function(function, *params):
    return function(*params)


# 根据参数层级组装函数
def use_function(function, function_id, params_level_list):
    # 解析出参数

    # 执行函数
    res = run_function(function)

    # 返回值封装进params_level_list

    return res

