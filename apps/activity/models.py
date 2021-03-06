# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from misc import parse_text


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
            f['fields']['rewards'] = parse_text(f['fields']['rewards'], 2)

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
            f['fields']['items'] = parse_text(f['fields']['items'], 2)

        return fixture


class OnlineTimeActivity(models.Model):
    id = models.IntegerField(primary_key=True)
    online_time = models.IntegerField()
    des = models.TextField(blank=True)
    rewards = models.TextField()

    class Meta:
        db_table = 'online_time_activity'
        verbose_name = '在线时长活动'
        verbose_name_plural = '在线时长活动'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['rewards'] = parse_text(f['fields']['rewards'], 2)

        return fixture

class ChallengeActivity(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.TextField(blank=True)
    rewards = models.TextField()

    class Meta:
        db_table = 'activity_challenge'
        verbose_name = '冲关活动'
        verbose_name_plural = '冲关活动'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['rewards'] = parse_text(f['fields']['rewards'], 2)

        return fixture

class PurchaseContinuesActivity(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.TextField()
    rewards = models.TextField()

    class Meta:
        db_table = 'purchase_continues_activity'
        verbose_name = '连续充值活动'
        verbose_name_plural = '连续充值活动'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['rewards'] = parse_text(f['fields']['rewards'], 2)

        return fixture


class LevelGrowingActivity(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.TextField()
    rewards = models.TextField()

    class Meta:
        db_table = 'level_growing_activity'
        verbose_name = '等级成长活动'
        verbose_name_plural = '等级成长活动'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['rewards'] = parse_text(f['fields']['rewards'], 2)

        return fixture
