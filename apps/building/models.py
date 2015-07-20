# -*- coding: utf-8 -*-

from django.db import models

class Building(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="名字")
    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'building'
        verbose_name = '设施'
        verbose_name_plural = '设施'


class BuildingLevels(models.Model):
    building = models.ForeignKey(Building, related_name='levels_info')
    level = models.IntegerField(verbose_name="等级", db_index=True)
    resource = models.CharField(max_length=255, blank=True, verbose_name="资源")
    up_need_club_level = models.IntegerField(verbose_name="升级所需俱乐部等级")
    up_need_gold = models.IntegerField(verbose_name="升级所需软妹币")
    value1 = models.IntegerField(null=True, blank=True, verbose_name="值1")
    des = models.CharField(max_length=255, blank=True, verbose_name="描述")

    def __unicode__(self):
        return u'#{0}'.format(self.level)

    class Meta:
        db_table = 'building_levels'
