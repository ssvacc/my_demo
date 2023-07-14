from django.http import JsonResponse
import pymysql
import datetime

from ReturnEnum import ReturnEnum
from app import models
# Create your tests here.
# 查询亚马逊星级大于4星的Asin，并给运营员及主管发待办
"""
1、查大于4星的asin  入参：4星、亚马逊平台；出参 ：asin + 站点  # SELECT shop_name, asin, shop_site, star FROM hq_db.t_amazon_listing_star WHERE star > 4 LIMIT 100
2、查询有哪些运营员   入参：asin + 站点，出参：运营员
3、查主管  入参：运营员  出参：主管
4、发待办  入参：运营员、主管、asin、内容、时间  出参：发送结果
"""


# 查大于4星的asin
def query_asin(params_dict):
    star = params_dict['star']
    return models.t_amazon_listing_star.objects.filter(star__gt=star).order_by("-id")[:10]


# 查有哪些运营人员
def query_seller(asin, shop_site):
    return models.t_amazon_asin_site_belong_details.objects.filter(asin=asin).filter(shop_site=shop_site).first()


# 根据列表查有哪些运营人员
def query_seller_by_params_dict(asin_set):
    seller_list = []
    for asin_obj in asin_set:
        seller_set = query_seller(asin_obj.asin, asin_obj.shop_site)
        seller_list.append(seller_set.seller)
    return seller_list


# 查主管
def query_group_leader(seller):
    db = pymysql.connect(host='hequpolardb-online-wr.rwlb.rds.aliyuncs.com',
                         user='hq_db_read_only',
                         password='K120Esc1',
                         database='hq_db')
    # 创建游标对象
    cursor = db.cursor()
    sql = "SELECT b.group_leader FROM hq_db.t_dingtalk_user_dept a, hq_db.t_dingtalk_first_level_department b WHERE a.Dept=b.first_level AND a.DelFlag = 0 AND a.Staff = '%s'" % seller
    result = {}
    try:
        cursor.execute(sql)  # 执行sql语句，也可执行数据库命令，如：show table
        # result = cursor.fetchall()[0]  # 查询主管
        result = cursor.fetchone()[0]  # 查询主管
    except Exception as e:
        db.rollback()
        print("查询失败")
        print(e)
    finally:
        cursor.close()  # 关闭当前游标
        db.close()  # 关闭数据库连接
    return result


# 查主管
def query_group_leader_by_list(seller_list):
    db = pymysql.connect(host='hequpolardb-online-wr.rwlb.rds.aliyuncs.com',
                         user='hq_db_read_only',
                         password='K120Esc1',
                         database='hq_db')
    # 创建游标对象
    cursor = db.cursor()
    leader_list = []
    try:
        for seller in seller_list:
            sql = "SELECT b.group_leader FROM hq_db.t_dingtalk_user_dept a, hq_db.t_dingtalk_first_level_department b WHERE a.Dept=b.first_level AND a.DelFlag = 0 AND a.Staff = '%s'" % seller
            cursor.execute(sql)  # 执行sql语句，也可执行数据库命令，如：show table
            leader_list.append(cursor.fetchone()[0])  # 查询主管
    except Exception as e:
        db.rollback()
        print("查询失败")
        print(e)
    finally:
        cursor.close()  # 关闭当前游标
        db.close()  # 关闭数据库连接
    return leader_list


# 发待办 运营员、主管、asin、内容、时间 出参：发送结果
def send(seller, leader, asin, content, time):
    res = {"code": ReturnEnum.SUCCESS().code, "msg": "Success!", "data": None}
    send_msg1 = "向" + seller + "发送待办。内容为：" + content + "。 发送时间：" + time + "，asin:" + asin
    print(send_msg1)
    send_msg2 = "向" + leader + "发送待办。内容为：" + content + "。 发送时间：" + time + "，asin:" + asin
    print(send_msg2)
    res["data"] = "发送成功"
    return res


def send_msg3(request):
    res = {"code": ReturnEnum.SUCCESS().code, "msg": "Success!", "data": None}
    params_dict = {}
    params_dict["star"] = 4
    # send_result_list = []
    # content = "这里是待办内容"
    # now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    #
    asin_set = query_asin(params_dict)
    # print(asin_set[0].asin)
    #
    seller_list = query_seller_by_params_dict(params_dict)
    #
    # leader_list = query_group_leader_by_list(seller_list)



    # send()
    # print(seller_list)

    # asin = asin_obj.asin
    # seller = seller_set.seller
    #
    # leader = query_group_leader(seller)
    #
    # send_result = send(seller, leader, asin, content, now_time)
    #
    #     send_result_list.append(send_result)
    # res["data"] = send_result_list
    return JsonResponse(res)




