# -*- coding: utf-8 -*-
from django.db import models


class t_public_function(models.Model):
    id = models.AutoField('id', primary_key=True)
    class_name = models.CharField('类名', max_length=255)
    function_name = models.CharField('函数名', max_length=255)
    function_desc = models.CharField('函数描述', max_length=255)
    function_detail = models.CharField('函数注释', max_length=500)
    author = models.CharField('函数作者', max_length=16)
    url = models.CharField('url', max_length=255)
    create_time = models.DateTimeField('创建时间')
    update_time = models.DateTimeField('更新时间', null=False)
    status = models.IntegerField('发布状态')
    release_person = models.CharField('审核人', max_length=16)
    release_time = models.DateTimeField('审核时间')
    publish_person = models.CharField('发布人', max_length=16)
    publish_time = models.DateTimeField('发布时间')
    s_principal = models.CharField('责任人', max_length=16)
    is_auto_test = models.IntegerField('是否加入自动化测试（0.未加入，1.已加入）')
    param_list = []
    return_list = []
    error_code_list = []

    class Meta:
        db_table = 't_public_function'

    def object_to_dict(self):
        create_time = self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None
        release_time = self.release_time.strftime('%Y-%m-%d %H:%M:%S') if self.release_time else None
        publish_time = self.publish_time.strftime('%Y-%m-%d %H:%M:%S') if self.publish_time else None
        return {
            "id": self.id,
            "class_name": self.class_name,
            "function_name": self.function_name,
            "function_desc": self.function_desc,
            "function_detail": self.function_detail,
            "author": self.author,
            "url": self.url,
            "status": self.status,
            "create_time": create_time,
            "release_person": self.release_person,
            "release_time": release_time,
            "publish_person": self.publish_person,
            "publish_time": publish_time,
            "s_principal": self.s_principal,
            "is_auto_test": self.is_auto_test,
            "param_list": self.param_list,
            "return_list": self.return_list,
            "error_code_list": self.error_code_list
        }
