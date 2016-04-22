# -*- coding: utf-8 -*-

from django.db import models


class NPCClubName(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'npc_club_name'
        verbose_name = "NPC俱乐部名字"
        verbose_name_plural = "NPC俱乐部名字"


    @classmethod
    def get_fixture_key(cls):
        return 'npc.NPCClubName'


class NPCManagerName(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'npc_manager_name'
        verbose_name = "NPC经理人名字"
        verbose_name_plural = "NPC经理人名字"

    @classmethod
    def get_fixture_key(cls):
        return 'npc.NPCManagerName'


class NPCClub(models.Model):
    id = models.IntegerField(primary_key=True)
    league = models.IntegerField(default=1, verbose_name="联赛等级")

    caozuo = models.CommaSeparatedIntegerField(blank=True, max_length=255, verbose_name="操作范围", help_text='low,high')
    baobing = models.CommaSeparatedIntegerField(blank=True, max_length=255, verbose_name="暴兵范围")
    jingying = models.CommaSeparatedIntegerField(blank=True, max_length=255, verbose_name="经营范围")
    zhanshu = models.CommaSeparatedIntegerField(blank=True, max_length=255, verbose_name="战术范围")

    skill_level = models.CommaSeparatedIntegerField(blank=True, max_length=255, verbose_name="技能等级范围")

    class Meta:
        db_table = 'npc_club'
        verbose_name = "NPC俱乐部"
        verbose_name_plural = "NPC俱乐部"

    @classmethod
    def get_fixture_key(cls):
        return 'npc.NPCClub'

    @classmethod
    def patch_fixture(cls, fixture):
        keys = ['caozuo', 'baobing', 'jingying', 'zhanshu', 'skill_level']
        for f in fixture:
            for key in keys:
                f['fields'][key] = [int(i) for i in f['fields'][key].split(',')]

        return fixture
