# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class BuyCost(models.Model):
    id = models.IntegerField(primary_key=True)
    cost = models.IntegerField()

    class Meta:
        db_table = 'energy_buy_cost'
        verbose_name = '体力购买花费'
        verbose_name_plural = '体力购买花费'