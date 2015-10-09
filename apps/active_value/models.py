# -*- coding: utf-8 -*-

from django.db import models

class ActiveReward(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='活跃度')
    package = models.ForeignKey('package.Package', verbose_name='物品包')

    class Meta:
        db_table = 'active_reward'
        verbose_name = '活跃度奖励'
        verbose_name_plural = '活跃度奖励'


class ActiveFunction(models.Model):
    id = models.CharField(primary_key=True, max_length=255, verbose_name='功能名字')
    function_sign = models.CharField(max_length=255, verbose_name='功能标识')
    value = models.IntegerField(verbose_name='每次奖励多少活跃度')
    max_times = models.IntegerField(verbose_name='每天最多奖励多少次')

    class Meta:
        db_table = 'active_function'
        verbose_name = '活跃度功能'
        verbose_name_plural = '活跃度功能'
