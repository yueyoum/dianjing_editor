# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Collection(models.Model):
    id = models.IntegerField(primary_key=True)
    talent_effect_id = models.IntegerField()

    class Meta:
        db_table = 'collection'
        verbose_name = '收集图鉴'
        verbose_name_plural = '收集图鉴'
