# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Dungeon(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="副本ID")
    name = models.CharField(max_length=32, verbose_name="副本名称")
    cost = models.IntegerField(verbose_name="消耗体力")
    open_time = models.CharField(max_length=32, verbose_name="开启时间",
                                 help_text="1,3,5 -- 周一、三、五开启")
    des = models.TextField(verbose_name="副本简介")

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
    belong = models.IntegerField(verbose_name="副本所属")
    power = models.IntegerField(verbose_name="参考战力")
    need_level = models.IntegerField(verbose_name="等级限制")
    drop = models.CharField(max_length=255, verbose_name="掉落配置",
                            help_text="物品ID,数量,掉落几率;物品ID,数量,掉落几率")
    npc_path = models.CharField(max_length=255, verbose_name="怪物配置",
                                help_text="位置,选手ID,兵种ID;位置,选手ID,兵种ID")
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
                _id, amount, _range = drop.split(',')
                drops.append([int(_id), int(amount), int(_range)])
            f['fields']['drop'] = drops

            npc_path = []
            for npc in f['fields']['npc_path'].split(';'):
                slot, staff, unit = npc.split(',')
                npc_path.append([int(slot), int(staff), int(unit)])
            f['fields']['npc_path'] = npc_path

        return fixture
