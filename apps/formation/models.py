# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Slot(models.Model):
    id = models.IntegerField(primary_key=True)
    club_level = models.IntegerField()
    des = models.TextField()

    class Meta:
        db_table = 'formation_slot'
        verbose_name = '阵型格子'
        verbose_name_plural = '阵型格子'
