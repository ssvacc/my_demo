# -*- coding: utf-8 -*-
from django.db import models

taskResultChoices = ((0, '失败'), (1, '成功'), (2, '未执行'))
scheduledChoices = ((0, '无定时任务'), (1, '有定时任务'))


class t_public_custom_function(models.Model):
    id = models.AutoField('id', primary_key=True)
    task_name = models.CharField('任务名称', max_length=255)
    task_desc = models.CharField('中文名', max_length=20)
    task_detail = models.CharField('任务详情', max_length=255)
    task_config_node = models.TextField('任务配置(节点)')
    task_config_link = models.TextField('任务配置(连线)')
    task_test_result = models.IntegerField('执行结果', choices=taskResultChoices)
    scheduled_tasks = models.IntegerField('是否有定时任务', choices=scheduledChoices)
    status = models.IntegerField('发布状态')
    create_person = models.CharField('创建人', max_length=16)
    create_time = models.DateTimeField('创建时间')
    update_time = models.DateTimeField('更新时间', null=False)
    release_person = models.CharField('发布人', max_length=16)
    release_time = models.DateTimeField('发布时间')
    function_list = []
    param_list = []
    return_list = []

    class Meta:
        verbose_name = u'软件规范'
        verbose_name_plural = verbose_name
        db_table = 't_public_custom_function'

    def object_to_dict(self):
        create_time = self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None
        release_time = self.release_time.strftime('%Y-%m-%d %H:%M:%S') if self.release_time else None
        return {
            "id": self.id,
            "task_name": self.task_name,
            "task_desc": self.task_desc,
            "task_detail": self.task_detail,
            "task_config_node": self.task_config_node,
            "task_config_link": self.task_config_link,
            "task_test_result": self.task_test_result,
            "scheduled_tasks": self.scheduled_tasks,
            "status": self.status,
            "create_person": self.create_person,
            "create_time": create_time,
            "release_person": self.release_person,
            "release_time": release_time,
            "function_list": self.function_list,
            "param_list": self.param_list,
            "return_list": self.return_list
        }
