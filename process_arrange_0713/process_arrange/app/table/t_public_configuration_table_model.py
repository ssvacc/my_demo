# -*- coding: utf-8 -*-
from django.db import models


class v_public_config_table(models.Model):
    table_id = models.CharField('表ID', max_length=4)
    field_id = models.CharField('字段ID', max_length=8)
    field_name = models.CharField('字段名', max_length=32)
    value = models.TextField('配置sql')

    class Meta:
        verbose_name = u'亚马逊市场营销系统'
        verbose_name_plural = verbose_name
        db_table = 'v_public_config_table'

    def object_to_dict(self):
        return {
            "i_deal_job_config_id": self.field_id,
            "s_name": self.field_name,
            "s_sql": self.value,
            "s_principal": "first_name字段",
        }
