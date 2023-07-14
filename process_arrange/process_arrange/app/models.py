# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


# class Params(models.Model):
#     id = models.AutoField('id', primary_key=True)
#     param_name = models.CharField('参数名', max_length=255)
#     param_desc = models.CharField('参数说明', max_length=255)
#     type = models.IntegerField('数据类型', max_length=1)
#
#     class Meta:
#         db_table = 'params'

    # def __unicode__(self):
    #     return u'%s' % (self.id,)


class t_amazon_listing_star(models.Model):
    shop_name = models.CharField(u'卖家简称', max_length=32, blank=True, null=True)
    shop_site = models.CharField(u'站点', max_length=64, blank=True, null=True)
    seller_sku = models.CharField(u'店铺sku', max_length=128, blank=True, null=True)
    asin = models.CharField(u'asin', max_length=32, blank=True, null=True)
    star = models.FloatField(u'星级', blank=True, null=True, default=0.0)
    num = models.IntegerField(u'评论数', blank=True, null=True, default=0)
    rate5 = models.IntegerField(u'五星占比', blank=True, null=True, default=0)
    rate4 = models.IntegerField(u'四星占比', blank=True, null=True, default=0)
    rate3 = models.IntegerField(u'三星占比', blank=True, null=True, default=0)
    rate2 = models.IntegerField(u'二星占比', blank=True, null=True, default=0)
    rate1 = models.IntegerField(u'一星占比', blank=True, null=True, default=0)
    refresh_time = models.DateTimeField(u'刷新时间', blank=True, null=True)
    insert_time = models.DateTimeField(u'刷新时间', auto_now=True, blank=True, null=True)
    flag = models.IntegerField(u'标识', blank=True, null=True, default=0)
    crawl_flag = models.IntegerField(u'成功标志', blank=True, null=True, default=0)

    class Meta:
        verbose_name = u'亚马逊星级评论数'
        verbose_name_plural = verbose_name
        db_table = 't_amazon_listing_star'

    # def __unicode__(self):
    #     return u'id:%s' % self.id


class t_amazon_asin_site_belong_details(models.Model):
    id = models.AutoField(u'流水号', primary_key=True)
    shop_site = models.CharField(u'站点', max_length=8, blank=True, null=True)
    asin = models.CharField(u'asin', max_length=32, blank=True, null=True)
    seller = models.CharField(u'运营员', max_length=64, blank=True, null=True)
    uploader = models.CharField(u'刊登人', max_length=64, blank=True, null=True)
    designer = models.CharField(u'设计师', max_length=64, blank=True, null=True)
    updatetime = models.DateTimeField(u'更新时间', blank=True, null=True)

    class Meta:
        verbose_name=u'AMZ链接归属详情(按asin+站点)'
        verbose_name_plural=verbose_name
        db_table = 't_amazon_asin_site_belong_details'
        ordering = ['-id']
    # def __unicode__(self):
    #     return u'id:%s'%(self.id)
