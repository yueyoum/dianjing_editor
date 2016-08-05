# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def _parse(text):
    res = []
    for x in text.split(';'):
        if not x:
            continue

        a, b = x.split(',')
        res.append((int(a), int(b)))
    return res

class NewPlayerActivity(models.Model):
    id = models.IntegerField(primary_key=True)
    day = models.IntegerField()
    name = models.CharField(max_length=255)

    condition_id = models.IntegerField()
    condition_value = models.IntegerField()

    rewards = models.TextField()
    show_progress = models.BooleanField()

    class Meta:
        db_table = 'activity_new_player'
        verbose_name = '新手活动'
        verbose_name_plural = '新手活动'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['rewards'] = _parse(f['fields']['rewards'])

        return fixture


class DailyBuy(models.Model):
    id = models.IntegerField(primary_key=True)
    items = models.TextField()
    diamond_original = models.IntegerField()
    diamond_now = models.IntegerField()

    class Meta:
        db_table = 'daily_buy'
        verbose_name = '每日购买'
        verbose_name_plural = '每日购买'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['items'] = _parse(f['fields']['items'])

        return fixture