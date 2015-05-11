# -*- coding: utf-8 -*-

from django.db import models

class NPCClub(models.Model):
    # RANK = (
    #     (1, "青铜三"),
    #     (2, "青铜二"),
    #     (3, "青铜一"),
    #     (4, "白银三"),
    #     (5, "白银二"),
    #     (6, "白银一"),
    #     (7, "黄金三"),
    #     (8, "黄金二"),
    #     (9, "黄金一"),
    # )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="俱乐部名字")
    manager_name = models.CharField(max_length=32, verbose_name="经理人名字")

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

    class Meta:
        db_table = 'npc_club'
        verbose_name = "NPC俱乐部"
        verbose_name_plural = "NPC俱乐部"
