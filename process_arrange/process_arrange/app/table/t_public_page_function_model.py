#    Copyright (c)  Fancyqube.com
#    @Author : niheng
#    @Date: 2023/3/14 下午5:10
#    @Description:
# -*- coding: utf-8 -*-
from django.db import models


class t_public_page_function(models.Model):
    id = models.AutoField('id', primary_key=True)
    page_name_en = models.CharField('页面英文名')
    page_name_cn = models.CharField('页面中文名')
    function_name_en = models.CharField("函数英文名")
    function_name_cn = models.CharField('函数中文名')

    class Meta:
        db_table = 't_public_page_function'

    def object_to_dict(self):
        return {
            "id": self.id,
            "page_name_en": self.page_name_en,
            "page_name_cn": self.page_name_cn,
            "function_name_en": self.function_name_en,
            "function_name_cn":self.function_name_cn
        }
