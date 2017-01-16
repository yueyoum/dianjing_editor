# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Dungeon(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="副本ID")
    name = models.CharField(max_length=32, verbose_name="副本名称")
    icon = models.CharField(max_length=32, verbose_name='ICON')
    cost = models.IntegerField(verbose_name="消耗体力")
    open_time = models.CharField(max_length=32, verbose_name="开启时间",
                                 help_text="1,3,5 -- 周一、三、五开启")
    open_des = models.TextField(verbose_name="开启描述")
    des = models.TextField(verbose_name="副本简介")
    map_name = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "dungeon"
        verbose_name = "副本"
        verbose_name_plural = "副本"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            open_time = []
            for weekday in f['fields']['open_time'].split(','):
                open_time.append(int(weekday))
            f['fields']['open_time'] = open_time

        return fixture


class DungeonGrade(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="副本等级ID")
    name = models.CharField(max_length=32, verbose_name="副本等级名")
    icon = models.CharField(max_length=255, blank=True)
    belong = models.IntegerField(verbose_name="副本所属")
    power = models.IntegerField(verbose_name="参考战力")
    need_level = models.IntegerField(verbose_name="等级限制")
    drop = models.TextField(max_length=255, verbose_name="掉落配置",
                            help_text="物品ID,数量,掉落几率;物品ID,数量,掉落几率")

    npc = models.IntegerField(default=0)
    des = models.TextField(verbose_name="副本等级描述")

    class Meta:
        db_table = "dungeon_grade"
        verbose_name = "副本等级"
        verbose_name_plural = "副本等级"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            drops = []
            for drop in f['fields']['drop'].split(';'):
                if not drop:
                    continue

                _id, amount, _range = drop.split(',')
                drops.append([int(_id), int(amount), int(_range)])
            f['fields']['drop'] = drops

        return fixture


class DungeonResetCost(models.Model):
    id = models.IntegerField(primary_key=True)
    dungeon_id = models.IntegerField()
    reset_times = models.IntegerField()
    diamond = models.IntegerField(verbose_name='钻石')

    class Meta:
        db_table = 'dungeon_reset_cost'
        verbose_name = "副本重置花费"
        verbose_name_plural = "副本重置花费"

    @classmethod
    def patch_fixture(cls, fixture):
        data = {}
        for f in fixture:
            dungeon_id = f['fields']['dungeon_id']
            if dungeon_id in data:
                data[dungeon_id].append((f['fields']['reset_times'], f['fields']['diamond']))
            else:
                data[dungeon_id] = [(f['fields']['reset_times'], f['fields']['diamond'])]

        new_fixture = []
        for k, v in data.iteritems():
            v.sort(key=lambda item: -item[0])
            x = {
                'pk': k,
                'fields': {
                    'times': v
                }
            }

            new_fixture.append(x)

        return new_fixture
