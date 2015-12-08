# -*- coding: utf-8 -*-

from django.db import models

class TrainingMatchReward(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="第几场")
    reward = models.ForeignKey('package.Package', verbose_name="奖励", related_name='tmr')
    additional_reward = models.ForeignKey('package.Package', null=True, blank=True, verbose_name="额外奖励", related_name='tmrar')
    des = models.TextField(blank=True)

    class Meta:
        db_table = 'training_match_reward'
        verbose_name = '训练赛奖励'
        verbose_name_plural = '训练赛奖励'

    @classmethod
    def patch_fixture(cls, fixtures):
        for f in fixtures:
            if not f['fields']['additional_reward']:
                f['fields']['additional_reward'] = 0
