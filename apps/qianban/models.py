# -*- coding: utf-8 -*-

from django.db import models

class QianBan(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, unique=True, verbose_name="名字")
    des = models.TextField(verbose_name="描述")

    class Meta:
        db_table = 'qianban'
        verbose_name = '牵绊'
        verbose_name_plural = "牵绊"

