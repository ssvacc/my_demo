# -*- coding: utf-8 -*-
from django.db import models


class t_public_function_param(models.Model):
    id = models.AutoField('id', primary_key=True)
    function_id = models.IntegerField('函数id')
    param_id = models.IntegerField('参数id')
    required = models.IntegerField('0.非必传，1.必传')
    type = models.IntegerField('0.返回码，1.参数，2.返回值')
    code_id = models.IntegerField('返回码id')
    example = models.CharField('参数示例', max_length=255)

    class Meta:
        db_table = 't_public_function_param'

    def object_to_dict(self):
        return {
            "id": self.id,
            "function_id": self.function_id,
            "param_id": self.param_id,
            "code_id": self.code_id,
            "required": self.required,
            "type": self.type,
            "example": self.example
        }
