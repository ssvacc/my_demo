# -*- coding: utf-8 -*-
from django.db import models


class t_public_custom_function_param(models.Model):
    id = models.AutoField('id', primary_key=True)
    task_id = models.IntegerField('功能id')
    param_id = models.IntegerField('参数id')
    param_name = models.CharField('参数名', max_length=255)
    param_desc = models.CharField('参数说明', max_length=255)
    data_type = models.IntegerField('数据类型')
    type = models.IntegerField('1.参数，2.返回值')

    class Meta:
        db_table = 't_public_custom_function_param'

    def object_to_dict(self):
        return {
            "id": self.id,
            "task_id": self.task_id,
            "param_id": self.param_id,
            "param_name": self.param_name,
            "param_desc": self.param_desc,
            "data_type": self.data_type,
            "type": self.type
        }
