# -*- coding: utf-8 -*-

from django.db import models

class BuildingNew(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    des = models.TextField()
    day_effect = models.CharField(max_length=255)
    night_effect = models.CharField(max_length=255)
    model_resource = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    class Meta:
        db_table = 'building_new'
        verbose_name = '建筑'
        verbose_name_plural = '建筑'
