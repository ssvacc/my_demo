#    Copyright (c)  Fancy qube.com
#    @Author : ni heng
#    @Date: 2023/6/08 下午15:40
#    @Description:
# -*- coding: utf-8 -*-
import functools

from app.function import execute_function


def InterfaceFunctionCheck(func):
    @functools.wraps(func)
    def wrapTheFunction(*args, **kwargs):
        function_id = kwargs.get('interface_function_id')
        function_name = kwargs.get('interface_function_name')
        # 有这俩个参数则需要做参数函数返回值校验
        if "interface_function_id" not in kwargs.keys():
            result = func(*args, **kwargs)
            return result
        kwargs.update({'function_id': function_id})
        kwargs.update({'function_name': function_name})
        kwargs.update({'func_obj': func})
        result, run_function_time = execute_function.auto_run_function(**kwargs)
        return result, run_function_time
    return wrapTheFunction
