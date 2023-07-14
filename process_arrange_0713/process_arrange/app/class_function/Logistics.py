# -*- coding: utf-8 -*-
# @Time : 2023-05-11
# @Author : Mr WangH
# @File : Logistics.py
import copy
import hashlib
import json
import requests
from ReturnEnum import ReturnEnum
# from ConstEnum import ELogistics, EProductEnter
# from global_cache_app.function.get_field_attr import FuncCacheWrapper
from ConstEnum import CommonSQL
from common_sql import execute_common_sql
from app.class_function.InterfaceFunction import InterfaceFunction




class KuaiDi100API(object):
    def __init__(self):
        self.key = 'onEvVvcu2066'  # TODO 客户授权key
        self.customer = 'D5845F130EBF648CA962382A931B093F'  # TODO 查询公司编号
        self.domain = 'https://poll.kuaidi100.com'

    def get_sign(self, param_str):
        # 签名加密， 用于验证身份， 按param + key + customer 的顺序进行MD5加密（注意加密后字符串要转大写）， 不需要“+”号
        temp_sign = param_str + self.key + self.customer
        md = hashlib.md5()
        md.update(temp_sign.encode())
        sign = md.hexdigest().upper()
        return sign

    def track(self, com, num, phone, ship_from="", ship_to=""):
        """
        物流轨迹实时查询
        :param com: 查询的快递公司的编码，一律用小写字母
        :param num: 查询的快递单号，单号的最大长度是32个字符
        :param phone: 收件人或寄件人的手机号或固话（也可以填写后四位，如果是固话，请不要上传分机号）
        :param ship_from: 出发地城市，省-市-区，非必填，填了有助于提升签收状态的判断的准确率，请尽量提供
        :param ship_to: 目的地城市，省-市-区，非必填，填了有助于提升签收状态的判断的准确率，且到达目的地后会加大监控频率，请尽量提供
        :return: requests.Response.text
        """
        res = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
        url = f'{self.domain}/poll/query.do'
        param = {
            'com': com,
            'num': num,
            'phone': phone,
            'from': ship_from,
            'to': ship_to,
            'resultv2': str(1),
            # 添加此字段表示开通行政区域解析功能。0：关闭（默认），1：开通行政区域解析功能，2：开通行政解析功能并且返回出发、目的及当前城市信息
            'show': str(0),  # 返回数据格式。0：json（默认），1：xml，2：html，3：text
            'order': 'desc'  # 返回结果排序方式。desc：降序（默认），asc：升序
        }
        try:
            param_str = json.dumps(param)  # 转json字符串
            sign = self.get_sign(param_str)
            request_data = {'customer': self.customer, 'param': param_str, 'sign': sign}
            response = requests.post(url, request_data)
            resp = response.json()
            if resp and resp.get("status") == str(requests.codes.ok) and resp.get("data"):
                res["code"] = ReturnEnum.ER_SUCCESS().code
                res["msg"] = ReturnEnum.ER_SUCCESS().msg
                res["data"] = resp
            else:
                res["msg"] = resp.get("message", "")
        except Exception as ex:
            res["msg"] = str(ex)

        return res


class Logistics(object):

    @staticmethod
    def get_logistics_company(s_logistics_no):
        """根据物流单号获取物流公司"""
        res = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
        s_logistics_no = str(s_logistics_no).strip()
        logistics_company_tuple = tuple()
        # for logistics_no_starts, logistics_company_info in ELogistics.E_logistics_no_company_dict.value.items():
        #     if s_logistics_no.startswith(logistics_no_starts):
        #         logistics_company_tuple = logistics_company_info
        #         break
        if logistics_company_tuple:
            res["code"] = ReturnEnum.ER_SUCCESS().code
            res["msg"] = ReturnEnum.ER_SUCCESS().msg
            res["data"] = {
                "s_logistics_company": logistics_company_tuple[0],
                "s_logistics_company_en": logistics_company_tuple[1]
            }
        else:
            res["code"] = ReturnEnum.ER_NO_DATA().code
            res["msg"] = ReturnEnum.ER_NO_DATA().msg
        return res

    @staticmethod
    # @FuncCacheWrapper(cache_time=10800)
    def get_logistics_trajectory(s_logistics_no, s_phone_end_no=""):
        """根据物流单号获取物流轨迹列表"""

        res = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
        try:
            get_logistics_company_res = Logistics.get_logistics_company(s_logistics_no=s_logistics_no)
            if get_logistics_company_res["code"] != ReturnEnum.ER_SUCCESS().code:
                res = get_logistics_company_res
            else:
                api_obj = KuaiDi100API()
                api_res = api_obj.track(com=get_logistics_company_res["data"].get("s_logistics_company_en", ""),
                                        num=s_logistics_no, phone=s_phone_end_no)
                if api_res["code"] != ReturnEnum.ER_SUCCESS().code:
                    res["msg"] = api_res["msg"]
                else:
                    a_logistics_trajectory = list()
                    for data_info in api_res["data"].get("data", list()):
                        a_logistics_trajectory.append({
                            "dt2_update_time": data_info["ftime"],
                            "s_logistics_context": data_info["context"],
                            "e_logistics_status": data_info["status"]
                        })
                    res["code"] = ReturnEnum.ER_SUCCESS().code
                    res["msg"] = ReturnEnum.ER_SUCCESS().msg
                    res["data"] = {
                        "a_logistics_trajectory": a_logistics_trajectory
                    }
        except Exception as ex:
            res["code"] = ReturnEnum.ER_SERVER_ERROR().code
            res["msg"] = ReturnEnum.ER_SERVER_ERROR().msg + str(ex)

        return res

    # @Author : zhouqiuyu
    @staticmethod
    # @FuncCacheWrapper(cache_time=10800)
    def get_logistics_surcharge_by_site_and_attr(**kwargs):
        """根据站点和物流属性获取附加费"""
        e_site, e_contra_band_attr = '', ''
        b_is_html = True
        if kwargs.get('e_site'):
            e_site = kwargs.get('e_site')
        if kwargs.get('e_contra_band_attr'):
            e_contra_band_attr = kwargs.get('e_contra_band_attr')
        if kwargs.get('b_is_html'):
            b_is_html = kwargs.get('b_is_html')
        res = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
        if not (e_site or e_contra_band_attr):
            res['code'] = ReturnEnum.ER_RISK_MISSING_PARAM().code
            res['msg'] = '缺少参数'
            return res
        if e_contra_band_attr in ELogistics.E_logistics_no_surcharge.value:
            a_logistics_surcharge = [{'e_logistics_channel': '', 'f_max_surcharge': 0, 'f_min_surcharge': 0}]
            res["code"] = ReturnEnum.ER_SUCCESS().code
            res["msg"] = ReturnEnum.ER_SUCCESS().msg
            res["data"] = {"a_logistics_surcharge ": a_logistics_surcharge}
            return res
        surcharge = '1'
        surchargeprice = surcharge + '_price'
        try:
            order_res = execute_common_sql(CommonSQL.LOGISTICS_SURCHARGE.value, (surchargeprice, surchargeprice, e_site), False).to_dict()
            if order_res['code'] == ReturnEnum.ER_SUCCESS().code and order_res['data']:
                s_html = ''
                if b_is_html:
                    title_res = InterfaceFunction().get_function_desc('Logistics::get_logistics_surcharge_by_site_and_attr')
                    if title_res['code'] != ReturnEnum.ER_SUCCESS().code:
                        res["msg"].msg = '获取函数名FN::get_warehouse_point_sales_data异常'
                    else:
                        s_function_name_cn = title_res['data']['s_function_name_cn']
                        o_function_param = title_res['data']['o_function_param']
                        html_dict_list = list()
                        for item in order_res['data']:
                            data_list = {'key': o_function_param['e_logistics_channel'], 'val': item['e_logistics_channel']}
                            html_dict_list.append(data_list)
                            data_list = {'key': o_function_param['f_max_surcharge'], 'val': item['f_max_surcharge']}
                            html_dict_list.append(data_list)
                            data_list = {'key': o_function_param['f_min_surcharge'], 'val': item['f_min_surcharge']}
                            html_dict_list.append(data_list)
                        s_html = ''
                res["code"] = ReturnEnum.ER_SUCCESS().code
                res["msg"] = ReturnEnum.ER_SUCCESS().msg
                res["data"] = {"a_logistics_surcharge ": order_res['data'], "s_html": s_html}
        except Exception as ex:
            res["code"] = ReturnEnum.ER_SERVER_ERROR().code
            res["msg"] = ReturnEnum.ER_SERVER_ERROR().msg + str(ex)
        return res
