# -*- coding: utf-8 -*-
from django.db import models

from ConstEnum import PUBLIC_CONFIG_INFO


class t_public_params(models.Model):
    id = models.AutoField('id', primary_key=True)
    param_name = models.CharField('英文名', max_length=255)
    param_desc = models.CharField('中文名', max_length=255)
    param_detail = models.CharField('注释', max_length=255)
    create_person = models.CharField('创建人', max_length=16)
    create_time = models.DateTimeField('创建时间')
    child_id = models.CharField('子级参数id(多个用逗号隔开)', max_length=255)
    select_info_id = models.IntegerField('枚举类型时，选中的t_online_select_info表id')
    data_type = models.IntegerField('数据类型')
    status = models.IntegerField('发布状态')
    release_person = models.CharField('发布人', max_length=32)
    release_time = models.DateTimeField('发布时间')
    apply_person = models.CharField('提交人', max_length=16)
    apply_time = models.DateTimeField('提交时间')
    child_list = []

    class Meta:
        db_table = 't_public_params'

    def object_to_dict(self):
        if self.child_id == '':
            self.child_id = None
        create_time = self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None
        release_time = self.release_time.strftime('%Y-%m-%d %H:%M:%S') if self.release_time else None
        apply_time = self.apply_time.strftime('%Y-%m-%d %H:%M:%S') if self.apply_time else None
        if PUBLIC_CONFIG_INFO.DEFAULT_EMPTY_DATE_TIME.value == apply_time:
            apply_time = None
        if PUBLIC_CONFIG_INFO.DEFAULT_EMPTY_DATE_TIME.value == release_time:
            release_time = None
        return {
            "id": self.id,
            "param_name": self.param_name,
            "param_desc": self.param_desc,
            "param_detail": self.param_detail,
            "create_person": self.create_person,
            "create_time": create_time,
            "child_id": self.child_id,
            "select_info_id": self.select_info_id,
            "data_type": self.data_type,
            "status": self.status,
            "release_person": self.release_person,
            "release_time": release_time,
            "apply_person": self.apply_person,
            "apply_time": apply_time,
            "child_list": self.child_list
        }