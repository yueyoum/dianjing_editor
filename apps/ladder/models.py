# -*- coding: utf-8 -*-

from django.db import models

class LadderLogTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    template = models.CharField(max_length=255, verbose_name="模板")

    class Meta:
        db_table = 'ladder_log_template'
        verbose_name = '天梯战况模板'
        verbose_name_plural = '天梯战况模板'



class LadderRankReward(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="排名上限")
    name = models.CharField(max_length=255)
    score = models.IntegerField(verbose_name="积分")
    package = models.ForeignKey('package.Package', null=True, blank=True, verbose_name="物品包")
    reward_des = models.TextField(verbose_name="奖励描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'ladder_rank_reward'
        verbose_name = "天梯排名奖励"
        verbose_name_plural = "天梯排名奖励"


class LadderScoreStore(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    times_limit = models.IntegerField(default=-1, verbose_name="次数限制",
                                      help_text="-1为没有限制，0为无法兑换，正整数N表示可以兑换N次")

    score = models.IntegerField(verbose_name="所需积分")
    package = models.ForeignKey('package.Package', verbose_name="物品包")

    class Meta:
        db_table = 'ladder_score_store'
        verbose_name = "天梯积分商店"
        verbose_name_plural = "天梯积分商店"


