#    Copyright (c)  Fancyqube.com
#    @Author : niheng
#    @Date: 2023/3/14 下午5:10
#    @Description:
# -*- coding: utf-8 -*-
from django.db import models


class t_public_page(models.Model):
    id = models.AutoField('id', primary_key=True)
    page_name_en = models.CharField('页面英文名')
    page_name_cn = models.CharField('页面中文名')
    create_person = models.CharField('创建人')
    create_time = models.DateTimeField('创建时间')

    class Meta:
        db_table = 't_public_page'

    def object_to_dict(self):
        return {
            "id": self.id,
            "page_name_en": self.page_name_en,
            "page_name_cn": self.page_name_cn,
            "create_person": self.create_person,
            "create_time":self.create_time,
        }
