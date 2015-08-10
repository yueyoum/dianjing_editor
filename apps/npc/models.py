# -*- coding: utf-8 -*-

from django.db import models

class NPCClubName(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'npc_club_name'
        verbose_name = "NPC俱乐部名字"
        verbose_name_plural = "NPC俱乐部名字"


class NPCManagerName(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'npc_manager_name'
        verbose_name = "NPC经理人名字"
        verbose_name_plural = "NPC经理人名字"



class NPCClub(models.Model):
    id = models.IntegerField(primary_key=True)
    league = models.ForeignKey('league.League', verbose_name="所属联赛等级")

    jingong_low = models.IntegerField(verbose_name="进攻下限")
    jingong_high = models.IntegerField(verbose_name="进攻上限")

    qianzhi_low = models.IntegerField(verbose_name="牵制下限")
    qianzhi_high = models.IntegerField(verbose_name="牵制上限")

    xintai_low = models.IntegerField(verbose_name="心态下限")
    xintai_high = models.IntegerField(verbose_name="心态上限")

    baobing_low = models.IntegerField(verbose_name="暴兵下限")
    baobing_high = models.IntegerField(verbose_name="暴兵上限")

    fangshou_low = models.IntegerField(verbose_name="防守下限")
    fangshou_high = models.IntegerField(verbose_name="防守上限")

    yunying_low = models.IntegerField(verbose_name="运营下限")
    yunying_high = models.IntegerField(verbose_name="运营上限")

    yishi_low = models.IntegerField(verbose_name="意识下限")
    yishi_high = models.IntegerField(verbose_name="意识上限")

    caozuo_low = models.IntegerField(verbose_name="操作下限")
    caozuo_high = models.IntegerField(verbose_name="操作上限")

    skill_low = models.IntegerField(verbose_name="技能等级下限")
    skill_high = models.IntegerField(verbose_name="技能等级上限")

    class Meta:
        db_table = 'npc_club'
        verbose_name = "NPC俱乐部"
        verbose_name_plural = "NPC俱乐部"
