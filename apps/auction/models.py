# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Auction(models.Model):
    id = models.IntegerField(primary_key=True)
    duration = models.IntegerField(verbose_name="出售时长")
    tax = models.IntegerField(verbose_name="出售税率")
    des = models.CharField(max_length=255, verbose_name="描述")

    class Meta:
        db_table = "auction"
        verbose_name = "拍卖"
        verbose_name_plural = "拍卖"
