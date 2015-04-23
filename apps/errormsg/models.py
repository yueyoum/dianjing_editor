# -*- coding: utf-8 -*-

from django.db import models

class ErrorMsg(models.Model):
    id = models.IntegerField(primary_key=True)
    error_index = models.CharField(max_length=64, unique=True)
    text_zh = models.CharField(max_length=255)

    des = models.CharField(max_length=255, default=0)

    class Meta:
        db_table = 'error_msg'
        verbose_name = '错误代码'
        verbose_name_plural = '错误代码'
