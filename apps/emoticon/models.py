# -*- coding: utf-8 -*-

from django.db import models

class Emoticon(models.Model):
    cmd = models.CharField(primary_key=True, max_length=255, verbose_name="命令")
    icon = models.CharField(max_length=255, verbose_name="图标")

    class Meta:
        db_table = 'emoticon'
        verbose_name = "表情"
        verbose_name_plural = "表情"
