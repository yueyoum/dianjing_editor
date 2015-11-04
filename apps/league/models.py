# -*- coding: utf-8 -*-

from django.db import models

class League(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="等级")
    name = models.CharField(max_length=255, verbose_name="名字")

    day_reward = models.ForeignKey('package.Package', related_name="league_day_reward", verbose_name="日奖励（赢）")
    day_reward_lose = models.ForeignKey('package.Package', null=True, blank=True, related_name="league_day_reward_lose", verbose_name="日奖励（输）")
    week_reward = models.ForeignKey('package.Package', related_name="league_week_reward", verbose_name="周奖励")

    des = models.TextField(blank=True, verbose_name='说明')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'league'
        verbose_name = "联赛"
        verbose_name_plural = "联赛"
