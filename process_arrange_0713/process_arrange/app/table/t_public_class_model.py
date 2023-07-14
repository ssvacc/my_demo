# -*- coding: utf-8 -*-
from django.db import models


class t_public_class(models.Model):
    id = models.AutoField('id', primary_key=True)
    class_name = models.CharField('类名（英文）', max_length=255)
    class_desc = models.CharField('类名（中文）', max_length=255)
    class_detail = models.CharField('类描述', max_length=255)
    create_person = models.CharField('创建人', max_length=16)
    create_time = models.DateTimeField('创建时间')

    class Meta:
        db_table = 't_public_class'

    def object_to_dict(self):
        create_time = self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None
        return {
            "id": self.id,
            "class_name": self.class_name,
            "class_desc": self.class_desc,
            "class_detail": self.class_detail,
            "create_person": self.create_person,
            "create_time": create_time,
        }
