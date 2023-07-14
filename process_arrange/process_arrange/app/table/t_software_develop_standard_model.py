# -*- coding: utf-8 -*-
from django.db import models


class t_software_develop_standard(models.Model):
    id = models.AutoField('id', primary_key=True)
    station = models.CharField('对应岗位', max_length=32, null=False, blank=False)
    standard_type = models.CharField('规范类别', max_length=1024, null=False, blank=False)
    standard_desc = models.TextField('规范明细', null=False, blank=False)
    example_pic = models.CharField('示例图片', max_length=1024, null=False, blank=True)
    remarks = models.TextField('备注信息', null=False, blank=True)
    apply_person = models.CharField('提交人', max_length=32, null=False, blank=False)
    apply_time = models.DateTimeField('提交时间', null=False, blank=True)
    update_person = models.CharField('更新人', max_length=32, null=False, blank=False)
    update_time = models.DateTimeField('更新时间', null=False, blank=True)

    class Meta:
        db_table = 't_software_develop_standard'

    def object_to_dict(self):
        return {
            "i_develop_require_specification_id": self.id,
            "e_develop_require_specification_station": self.station,
            "e_develop_require_specification_type": self.standard_type,
            "s_desc": self.standard_desc,
            "s_pic_url": self.example_pic,
            "s_remarks": self.remarks,
            "s_apply_person": self.apply_person,
            "dt2_apply_time": self.apply_time.strftime('%Y-%m-%d %H:%M:%S'),
            "s_update_person": self.update_person,
            "dt2_update_time": self.update_time.strftime('%Y-%m-%d %H:%M:%S')
        }
