#    Copyright (c)  Fancyqube.com
#    @Author : chenshuo
#    @Date: 2023/7/11 下午8:10
#    @Description:
# -*- coding: utf-8 -*-
from django.db import models


class t_public_params_field(models.Model):
    id = models.AutoField('id', primary_key=True)
    param_id = models.IntegerField('参数id')
    param_name = models.CharField('参数英文名', max_length=64)
    param_desc = models.CharField('参数中文名', max_length=64)
    field_param_id = models.IntegerField('字段参数id')
    field_param_name = models.CharField('字段参数英文名', max_length=64)
    field_param_desc = models.CharField('字段参数中文名', max_length=64)
    field_value = models.TextField('字段值')
    class Meta:
        db_table = 't_public_params_field'

    def object_to_dict(self):
        return {
            "id": self.id,
            "param_id": self.param_id,
            "param_name": self.param_name,
            "param_desc": self.param_desc,
            "field_param_id": self.field_param_id,
            "field_param_name": self.field_param_name,
            "field_param_desc": self.field_param_desc,
            "field_value": self.field_value
        }
