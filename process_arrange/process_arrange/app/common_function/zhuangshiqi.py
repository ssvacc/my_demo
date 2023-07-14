import functools



class FuncCacheWrapper(object):
    """不可与 AsyncAdmin 同时使用"""
    def __init__(self, cache_time=300, definer="", class_method=False):
        self.cache_time = cache_time
        self.definer = str(definer).strip()
        self.class_method = class_method  # 给类方法缓存

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper_handle(*args, **kwargs):
            print('FuncCacheWrapper ==> func.__code__.co_varnames')
            print('FuncCacheWrapper:args')
            print(args)
            print('FuncCacheWrapper:kwargs')
            print(kwargs)
            print(func.__code__.co_varnames)
            func_res = func(*args, **kwargs)
            return func_res
        return wrapper_handle

