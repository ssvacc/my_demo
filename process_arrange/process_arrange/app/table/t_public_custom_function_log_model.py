# -*- coding: utf-8 -*-
from django.db import models


class t_public_custom_function_log(models.Model):
    id = models.AutoField('id', primary_key=True)
    table_id = models.IntegerField('关联表id')
    old_name = models.CharField('原名称', max_length=255)
    new_name = models.CharField('新名称', max_length=255)
    old_desc = models.CharField('原描述', max_length=255)
    new_desc = models.CharField('新描述', max_length=255)
    action_user = models.CharField('操作人', max_length=64)
    action_time = models.DateTimeField('操作时间')
    action_type = models.IntegerField('操作类型(0.删除,1.新增,2.修改)')
    table_type = models.IntegerField('表名(0.类名表,1.参数表,2.函数表,3.功能表,4.返回码表)')

    class Meta:
        db_table = 't_public_custom_function_log'

    def object_to_dict(self):
        return {
            "id": self.id,
            "table_id": self.table_id,
            "old_name": self.old_name,
            "new_name": self.new_name,
            "old_desc": self.old_desc,
            "new_desc": self.new_desc,
            "action_user": self.action_user,
            "action_time": self.action_time,
            "action_type": self.action_type,
            "table_type": self.table_type
        }
