# -*- coding: utf-8 -*-

from django.db import models

class Function(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    belong_to_building = models.ForeignKey('building.Building', null=True, blank=True, verbose_name="所属建筑")
    order_in_building = models.IntegerField(default=1, verbose_name="在界面中显示顺序")
    need_building_level = models.IntegerField(default=1, verbose_name="所需建筑等级")
    unlock_des = models.TextField(blank=True, verbose_name="解锁描述")


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'function'
        verbose_name = "功能"
        verbose_name_plural = "功能"

