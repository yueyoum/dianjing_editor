# -*- coding: utf-8 -*-

from django.db import models

class Notification(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    template = models.TextField()

    class Meta:
        db_table = 'notification'
        verbose_name = '通知'
        verbose_name_plural = '通知'
