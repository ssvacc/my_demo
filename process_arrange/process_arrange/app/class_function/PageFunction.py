import ConstEnum
from ReturnEnum import ReturnEnum
from app.common_function import db_util
from app.table.other_app_table.t_online_select_info import t_online_select_info as TOnlineSelectInfo
from app.table.t_public_params_model import t_public_params as TPublicParams

class PageFunction(object):
    # 根据枚举名称获取枚举选项列表
    @staticmethod
    def get_enum_options_by_name(s_enum_name, **kwargs):
        result = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": {}}
        try:
            if not s_enum_name:
                result['code'] = ReturnEnum.ER_PARAMENTER().code
                result['msg'] = ReturnEnum.ER_PARAMENTER().msg
                return result
            enum_param = TPublicParams.objects.filter(data_type=ConstEnum.FuncProcessCode.ENUM_DATA_TYPE.value).filter(param_name=s_enum_name).first()
            if not enum_param:
                result['code'] = ReturnEnum.ER_NO_DATA().code
                result['msg'] = ReturnEnum.ER_NO_DATA().msg
                return result
            i_enum_id = enum_param.select_info_id
            enum = TOnlineSelectInfo.objects.filter(id=i_enum_id).first()
            if not enum:
                result['code'] = ReturnEnum.ER_NO_DATA().code
                result['msg'] = ReturnEnum.ER_NO_DATA().msg
                return result
            sql = enum.get_info_sql
            conn = db_util.SQLConn().conn_to_mysql()
            cursor = conn.cursor()
            cursor.execute(sql)
            query_data = cursor.fetchall()
            a_enum_option = []
            for item in query_data:
                option = {}
                option['s_enum_key'] = item[0]
                option['s_enum_value'] = item[0]
                option['s_enum_variable_name'] = None
                if len(item) > 1:
                    option['s_enum_value'] = item[1]
                if len(item) == 3:
                    option['s_enum_variable_name'] = item[2]
                a_enum_option.append(option)
            result['code'] = ReturnEnum.ER_SUCCESS().code
            result['msg'] = ReturnEnum.ER_SUCCESS().msg
            result['data']['a_enum_option'] = a_enum_option
        except Exception as e:
            result['msg'] += str(e)
        return result