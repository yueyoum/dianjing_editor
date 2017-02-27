# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class UI(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    icon = models.CharField(max_length=255)
    des = models.TextField()

    class Meta:
        db_table = 'ui'

class BackgroundImage(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.CharField(max_length=255)

    class Meta:
        db_table = 'background_image'
        verbose_name = '背景图片'
        verbose_name_plural = '背景图片'