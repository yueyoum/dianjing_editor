# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class NPCFormation(models.Model):
    id = models.IntegerField(primary_key=True)
    staffs = models.CharField(max_length=255, help_text='位置,选手id,兵种id;')

    class Meta:
        db_table = 'npc_formation'
        verbose_name = 'NPC阵型'
        verbose_name_plural = "NPC阵型"
