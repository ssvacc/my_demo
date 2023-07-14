# -*- coding: utf-8 -*-
from django.db import models


class t_public_custom_function_relevance(models.Model):
    id = models.AutoField('id', primary_key=True)
    task_id = models.IntegerField('功能id')
    function_id = models.IntegerField('函数id')
    function_order = models.IntegerField('函数顺序')

    class Meta:
        db_table = 't_public_custom_function_relevance'

    def object_to_dict(self):
        return {
            "id": self.id,
            "task_id": self.task_id,
            "function_id": self.function_id,
            "function_order": self.function_order
        }
