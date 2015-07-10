# -*- coding: utf-8 -*-

from django.db import models

class ClubFlag(models.Model):
    id = models.IntegerField(primary_key=True)
    flag = models.CharField(max_length=255, verbose_name="旗帜")

    class Meta:
        db_table = 'club_flag'
        verbose_name = "俱乐部图标"
        verbose_name_plural = "俱乐部图标"
