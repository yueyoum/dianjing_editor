# -*- coding: utf-8 -*-

from django.db import models


class League(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="等级")
    name = models.CharField(max_length=255, verbose_name="名字")
    daily_reward = models.ForeignKey('package.Package', related_name="league_daily_reward", verbose_name="每日奖励")
    up_need_score = models.IntegerField(verbose_name="晋级积分")
    des = models.TextField(blank=True, verbose_name='说明')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'league'
        verbose_name = "联赛"
        verbose_name_plural = "联赛"
