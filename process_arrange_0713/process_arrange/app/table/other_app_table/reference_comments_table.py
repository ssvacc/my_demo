# -*- coding: utf-8 -*-
# @Time : 2023-01-30
# @Author : Mr WangH
# @File : reference_comments_table.py


from django.db import models
# global_cache_app/table/reference_comments_table.py

class t_online_comment_info(models.Model):
    id = models.AutoField('id', primary_key=True)
    app_label = models.CharField("app_label", max_length=32, default="", blank=True, null=False)
    model_name = models.CharField("model_name", max_length=64, default="", blank=True, null=False)
    data_id = models.IntegerField("data_id", default=0, blank=True, null=False)
    comment_time = models.DateTimeField("评论时间", blank=True, null=True)
    comment_person = models.CharField("评论人", max_length=16, default="", blank=True, null=False)
    comment_desc = models.CharField("评论内容", max_length=1024, default="", blank=True, null=False)
    model_cn_name = models.CharField("model中文名", max_length=128, default="", blank=True, null=False)
    # comment_mention_list = []

    class Meta:
        verbose_name = u'评论数据'
        verbose_name_plural = verbose_name
        db_table = 't_online_comment_info'

    def object_to_dict(self):
        comment_time = self.comment_time.strftime('%Y-%m-%d %H:%M:%S') if self.comment_time else None
        return {
            "id": self.id,
            "data_id": self.data_id,
            "comment_time": comment_time,
            "comment_person": self.comment_person,
            "comment_desc": self.comment_desc,
            "model_cn_name": self.model_cn_name
        }

class t_online_comment_mention(models.Model):
    id = models.AutoField('id', primary_key=True)
    comment_id = models.IntegerField("comment_id", default=0, blank=True, null=False)
    mention_person = models.CharField("提及人", max_length=16, default="", blank=True, null=False)
    mention_read = models.IntegerField("是否已读", default=0, choices=((0, "未读"), (1, "已读")), blank=True, null=False)
    read_time = models.DateTimeField("已读时间", blank=True, null=True)

    class Meta:
        verbose_name = u'提及数据'
        verbose_name_plural = verbose_name
        db_table = 't_online_comment_mention'

    def object_to_dict(self):
        read_time = self.read_time.strftime('%Y-%m-%d %H:%M:%S') if self.read_time else None
        return {
            "id": self.id,
            "comment_id": self.comment_id,
            "mention_person": self.mention_person,
            "mention_read": self.mention_read,
            "read_time": read_time
        }
