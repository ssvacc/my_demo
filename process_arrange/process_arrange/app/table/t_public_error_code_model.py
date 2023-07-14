# -*- coding: utf-8 -*-
from django.db import models


class t_public_error_code(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField('变量名', max_length=64)
    code = models.IntegerField('code')
    msg = models.CharField('msg', max_length=128)
    author = models.CharField('作者', max_length=16)
    status = models.IntegerField('发布状态')
    create_time = models.DateTimeField('创建时间')
    update_time = models.DateTimeField('更新时间')

    class Meta:
        db_table = 't_public_error_code'

    def object_to_dict(self):
        create_time = self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None
        update_time = self.update_time.strftime('%Y-%m-%d %H:%M:%S') if self.update_time else None
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "msg": self.msg,
            "author": self.author,
            "status": self.status,
            "create_time": create_time,
            "update_time": update_time
        }
