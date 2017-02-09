# -*- coding: utf-8 -*-

from django.db import models

class BroadcastTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    template = models.TextField()

    class Meta:
        db_table = 'broadcast_template'
        verbose_name = '广播模板'
        verbose_name_plural = '广播模板'