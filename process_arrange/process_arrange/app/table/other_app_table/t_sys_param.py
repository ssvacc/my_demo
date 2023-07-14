# -*- coding: utf-8 -*-
from django.db import models


class t_sys_param(models.Model):
    Type = models.CharField(u'参数类型', max_length=12, blank=True, null=True, help_text='数字类型编码, 相同的编码表示为统一类型')
    TypeDesc = models.CharField(u'参数类型描述', max_length=32, blank=True, null=True, help_text='一般为英文解释, 表示这一类型的属性')
    TypeName = models.CharField(u'参数类型名称', max_length=32, blank=True, null=True, help_text='一般为中文描述, 表示这一类型的用途')
    Seq = models.IntegerField(u'参数序号', blank=True, null=True, help_text='无实际意义,一般用来排序')
    V = models.CharField(u'参数值', max_length=255, blank=True, null=True, help_text='填写你需要的值,比如类型,姓名等')
    VDesc = models.TextField(u'参数值描述', blank=True, null=True, help_text='填写对你需要值的补充，可以和参数值相同，也可以不同')
    UpdateTime = models.DateTimeField(u'更新时间', auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = u'系统参数配置'
        verbose_name_plural = u'系统参数配置'
        db_table = 't_sys_param'
        ordering = ['Type', 'Seq']

    def __unicode__(self):
        return u'%s' % (self.id)


class public_config_table_filed(models.Model):
    table_id = models.CharField(u'table_id', max_length=32, blank=True, null=True)
    field_id = models.CharField(u'table_id', max_length=32, blank=True, null=True)
    field_name = models.CharField(u'field_name', max_length=32, blank=True, null=True)

    class Meta:
        verbose_name = u'public_config_table_filed'
        verbose_name_plural = u'public_config_table_filed'
        db_table = 'public_config_table_filed'


class t_sys_param_collect_display(models.Model):
    id = models.IntegerField(primary_key=True)
    Type = models.CharField(u'参数类型', max_length=32, blank=True, null=True)
    description = models.CharField(u'描述', max_length=255, blank=True, null=True)
    collectors = models.CharField(u'收藏人', max_length=32, blank=True, null=True)
    collect_time = models.DateTimeField(u'收藏时间', max_length=32, blank=True, null=True)

    class Meta:
        verbose_name = u'系统参数收藏'
        db_table = 't_sys_param_collect_display'
