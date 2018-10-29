# Create your models here.
# # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class english_dict(models.Model):
    '''
    词库表,存放不同词库
    '''
    dict_name = models.CharField(max_length=100, verbose_name="词库名")
    details = models.TextField(blank=True, verbose_name="词库详情描述")
    words = models.TextField(blank=True, verbose_name="词库单词列表")

    def __str__(self):
        return self.dict_name

    class Meta:
        verbose_name_plural = '词库表'


class score(models.Model):
    '''
    用户对各词库学习详情
    '''
    username = models.CharField(max_length=100, verbose_name="用户名")
    dict_name = models.CharField(max_length=100, verbose_name="词库名")
    learned_words = models.TextField(blank=True, verbose_name="已学习单词列表")

    class Meta:
        verbose_name_plural = '学习详情表'
