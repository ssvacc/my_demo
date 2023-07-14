# -*- coding: utf-8 -*-
from datetime import datetime
from app.table.t_software_develop_standard_model import t_software_develop_standard
from ReturnEnum import ReturnEnum


class DevelopRequireSpecification:
    @staticmethod
    #  全量查询所有数据
    def get_all(**kwargs):
        res = {"code": ReturnEnum.ER_FAIL().code, "msg": ReturnEnum.ER_FAIL().msg, "data": dict()}
        t_software_develop_standard_list = t_software_develop_standard.objects.all().order_by('-update_time')
        if not t_software_develop_standard_list:
            res['code'] = ReturnEnum.ER_NO_DATA().code
            res['msg'] = ReturnEnum.ER_NO_DATA().msg
            res['data'] = None
        else:
            data_list = []
            for item in t_software_develop_standard_list:
                data_item = item.object_to_dict()
                data_list.append(data_item)
            res['code'] = ReturnEnum.ER_SUCCESS().code
            res['msg'] = ReturnEnum.ER_SUCCESS().msg
            res['data']['a_develop_require_specification'] = data_list
        return res

    # 新增数据并返回结果
    @staticmethod
    def add(o_develop_require_specification, s_operator, **kwargs):
        try:
            count = t_software_develop_standard.objects.filter(
                standard_desc=o_develop_require_specification.get('s_desc')).count()
            if count > 0:
                res = {'code': ReturnEnum.ER_DATA_ALREADY_EXISTS().code,
                       'msg': o_develop_require_specification.get('s_desc') + ReturnEnum.ER_DATA_ALREADY_EXISTS().msg}
                return res
            t_software_develop_standard.objects.create(station=o_develop_require_specification.get('e_develop_require_specification_station', ''),
                                                       standard_type=o_develop_require_specification.get('e_develop_require_specification_type', ''),
                                                       standard_desc=o_develop_require_specification.get('s_desc', ''),
                                                       remarks=o_develop_require_specification.get('s_remarks', ''),
                                                       example_pic='',
                                                       apply_person=s_operator,
                                                       apply_time=datetime.now(),
                                                       update_person=s_operator,
                                                       update_time=datetime.now())
            res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "新增成功!", "data": dict()}
        except:
            res = {"code": ReturnEnum.ER_SERVER_ERROR().code, "msg": ReturnEnum.ER_SERVER_ERROR().msg, "data": dict()}
        return res

    # 编辑规范函数
    @staticmethod
    def edit(o_develop_require_specification, s_operator, **kwargs):
        try:
            count = t_software_develop_standard.objects.filter(id=o_develop_require_specification.get('i_develop_require_specification_id')).count()
            if count == 0:
                res = {'code': ReturnEnum.ER_DATA_NOT_EXISTS().code,
                       'msg': ReturnEnum.ER_DATA_NOT_EXISTS().msg}
                return res
            standards_id = o_develop_require_specification.get('i_develop_require_specification_id')
            standards = t_software_develop_standard.objects.get(id=standards_id)
            standards.station = o_develop_require_specification.get('e_develop_require_specification_station')
            standards.standard_type = o_develop_require_specification.get('e_develop_require_specification_type')
            standards.standard_desc = o_develop_require_specification.get('s_desc')
            standards.remarks = o_develop_require_specification.get('s_remarks')
            standards.update_time = datetime.now()
            standards.update_person = s_operator
            standards.save()
            res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "操作成功!", "data": dict()}
        except:
            res = {"code": ReturnEnum.ER_SERVER_ERROR().code, "msg": ReturnEnum.ER_SERVER_ERROR().msg, "data": dict()}
        return res

    # 删除规范函数
    @staticmethod
    def delete(i_develop_require_specification_id, **kwargs):
        try:
            standard_obj = t_software_develop_standard.objects.filter(id=i_develop_require_specification_id).first()
            standard_obj.delete()
            res = {"code": ReturnEnum.ER_SUCCESS().code, "msg": "删除成功!", "data": dict()}
        except:
            res = {"code": ReturnEnum.ER_SERVER_ERROR().code, "msg": ReturnEnum.ER_SERVER_ERROR().msg, "data": dict()}
        return res