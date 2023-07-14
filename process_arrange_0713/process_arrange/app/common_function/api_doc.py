# -*- coding: utf-8 -*-
# Editer: 程子瑞
# 自定义API文档注解

from functools import wraps


# API主注解
# description:描述
# author:维护人
def api_doc(description, author):
    def decorate(func):
        if not hasattr(func, 'api_doc'):
            func.api_doc = {}
        func.api_doc['description'] = description
        func.api_doc['author'] = author

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorate


# 请求参数注解
def api_doc_param(filed, type, description, requried=False, example="", remark=""):
    def decorate(func):
        if not hasattr(func, 'api_doc'):
            func.api_doc = {}
        if not 'param' in func.api_doc.keys():
            func.api_doc['param'] = []
        func.api_doc['param'].insert(0,{
            'filed': filed,
            'type': type,
            'description': description,
            'requried': requried,
            'example': example,
            'remark': remark,
        })

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorate

# 返回参数注解
def api_doc_return_param(filed, type, description,example="", remark=""):
    def decorate(func):
        if not hasattr(func, 'api_doc'):
            func.api_doc = {}
        if not 'return_param' in func.api_doc.keys():
            func.api_doc['return_param'] = []
        func.api_doc['return_param'].insert(0,{
            'filed': filed,
            'type': type,
            'description': description,
            'example': example,
            'remark': remark,
        })

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorate

# 返回值注解
# type:返回值类型，例如string
# example:返回值例子（json格式），例如
'''
{
    "code": 0,
    "msg": "",
    "data": [
        {
            "product_title": "不锈钢爱心角架厨房浴室置物架加厚三角架收纳架双层架子耐用--违禁品",
            "third_platform": "4PX",  
            "product_sku": "VBA2817",
            "CreateMan": "熊志云",
            "CreateDate": "2021-05-07T14:45:03", 
            "sku_picture": [
                "https://fancyqube-kc-csv.oss-cn-shanghai.aliyuncs.com/images/VBA2817.jpg"
            ],
            "product_status": "待审核", 
            "commodity_mark": "(VBA2817*1)*1" 
        }
    ]
}
'''
def api_doc_return(type, example, remark = ""):
    def decorate(func):
        if not hasattr(func, 'api_doc'):
            func.api_doc = {}
        func.api_doc['return_type'] = type
        func.api_doc['return_example'] = example
        func.api_doc['remark'] = remark

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorate



