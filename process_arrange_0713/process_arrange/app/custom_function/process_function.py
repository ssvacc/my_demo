
import pymysql

# 本地执行查询语句
from ReturnEnum import ReturnEnum


def run_query_sql(SQL):
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='root',
                         database='process_arrange')
    # 创建游标对象
    cursor = db.cursor()
    # sql = "SELECT b.group_leader FROM hq_db.t_dingtalk_user_dept a, hq_db.t_dingtalk_first_level_department b WHERE a.Dept=b.first_level AND a.DelFlag = 0 AND a.Staff = '%s'" % seller
    sql = SQL
    result = ReturnEnum.ER_SUCCESS()
    try:
        cursor.execute(sql)  # 执行sql语句，也可执行数据库命令，如：show table
        result.data = cursor.fetchall()
    except Exception as e:
        db.rollback()
        print("查询失败")
        print(e)
    finally:
        cursor.close()  # 关闭当前游标
        db.close()  # 关闭数据库连接
    return result


