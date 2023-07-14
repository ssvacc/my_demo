# # -*- coding: utf-8 -*-
# # Editer: 程子瑞
#
from ReturnEnum import ReturnEnum

import pymysql
#
def execute_common_sql(id, params, is_update=False, is_sqlserver=False, is_main=False):
    sql = "select id,name,code,msg,author,status,create_time,update_time from t_public_error_code order by left(code + 1,1),  (code + 1); "
    res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": ReturnEnum.ER_SUCCESS().msg, "data": dict()}
    try:
        conn = pymysql.connect(host='hequpolardb-online-wr.rwlb.rds.aliyuncs.com',
                             user='hq_db_read_only',
                             password='K120Esc1',
                             database='hq_db')
        # 创建游标对象
        cursor = conn.cursor()
        cursor.execute(sql)
        if is_update:
            conn.commit()
        else:
            res['data'] = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        import traceback
        res = ReturnEnum.ER_DB()
        res.msg = traceback.format_exc()
    return res
