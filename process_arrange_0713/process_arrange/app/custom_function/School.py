from ReturnEnum import ReturnEnum
from app.common_function.zhuangshiqi import FuncCacheWrapper
from app.custom_function.Area import Area
from app.function.interfaceFunctionCheck import InterfaceFunctionCheck


class School():
    def __init__(self):
        pass


    # @api_doc(description="获取SPU风险等级", author="李志华")
    @staticmethod
    @FuncCacheWrapper(cache_time=10)
    @InterfaceFunctionCheck
    def show_school_location_static(s_school_name, s_location, **kwargs):
        print('function == > show_school_location_static')
        welcome = "欢迎来到" + str(s_school_name)
        try:
            Area_obj = Area(id=1, area_name=s_location)
            show = Area_obj.show_area_name()
        except Exception as e:
            res = {"code": ReturnEnum.ER_FAIL().code,
                   "msg": ReturnEnum.ER_FAIL().msg, "data": None}
            return res
        res = {"code": ReturnEnum.ER_SUCCESS().code,
               "msg": ReturnEnum.ER_SUCCESS().msg, "data": dict()}
        res['data']['welcome'] = show + welcome
        return res

    def show_school_location(self, s_school_name, s_location, **kwargs):
        welcome = "欢迎来到"
        try:
            Area_obj = Area(id=1, area_name='s_location')
            a = 2 / 0
            show = Area_obj.show_area_name()
        except Exception as e:
            res = {"code": ReturnEnum.ER_FAIL().code,
                   "msg": ReturnEnum.ER_FAIL().msg, "data": None}
            return res
        res = {"code": ReturnEnum.ER_SUCCESS().code,
               "msg": ReturnEnum.ER_SUCCESS().msg, "data": dict()}
               # "msg": ReturnEnum.ER_SUCCESS().msg, "data": None}
        res['data']['welcome'] = show + welcome
        return res
