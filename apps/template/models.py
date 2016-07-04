# -*- coding: utf-8 -*-

from django.db import models

class SponsorLogTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    template = models.TextField()

    class Meta:
        db_table = 'sponsor_log_template'
        verbose_name = '赞助信息模板'
        verbose_name_plural = '赞助信息模板'


class BroadcastTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    template = models.TextField()

    class Meta:
        db_table = 'broadcast_template'
        verbose_name = '广播模板'
        verbose_name_plural = '广播模板'