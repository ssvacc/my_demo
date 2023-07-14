# -*- coding: utf-8 -*-
from django.db import models

class t_online_select_info(models.Model):
    id = models.IntegerField('id', primary_key=True)
    user_key = models.CharField('user_key', max_length=255)
    name = models.CharField('name', max_length=255)
    get_info_sql = models.CharField('get_info_sql', max_length=2000)
    key_val = models.CharField('key_val', max_length=255)
    db_type = models.IntegerField('选取db', max_length=11)

    class Meta:
        db_table = 't_online_select_info'

    def object_to_dict(self):
        return {
            "id": self.id,
            "user_key": self.user_key,
            "name": self.name,
            "get_info_sql": self.get_info_sql,
            "key_val": self.key_val,
            "db_type": self.db_type
        }
