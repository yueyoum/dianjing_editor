# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ArenaNPC(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='排名上限')
    npcs = models.CommaSeparatedIntegerField(max_length=255)

    class Meta:
        db_table = 'arena_npc'
        verbose_name = '竞技场NPC'
        verbose_name_plural = "竞技场NPC"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['npcs'] = [int(i) for i in f['fields']['npcs'].split(',')]

        return fixture


class HonorReward(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='荣耀点')
    reward = models.CharField(max_length=255, help_text='id,amount;id,amount')

    class Meta:
        db_table = 'arena_honor_reward'
        verbose_name = '荣耀积分奖励'
        verbose_name_plural = "荣耀积分奖励"

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse_reward(text):
            result = []
            for x in text.split(';'):
                _a, _b = x.split(',')
                result.append((int(_a), int(_b)))

        for f in fixture:
            f['fields']['reward'] = _parse_reward(f['fields']['reward'])

        return fixture


class RankReward(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='排名上限')
    reward = models.CharField(max_length=255, help_text='id,amount;id,amount')
    mail_title = models.CharField(max_length=255)
    mail_content = models.CharField(max_length=255)

    class Meta:
        db_table = 'arena_rank_reward'
        verbose_name = '排名奖励'
        verbose_name_plural = "排名奖励"

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse_reward(text):
            result = []
            for x in text.split(';'):
                _a, _b = x.split(',')
                result.append((int(_a), int(_b)))

        for f in fixture:
            f['fields']['reward'] = _parse_reward(f['fields']['reward'])

        return fixture


class MatchReward(models.Model):
    TYPE = (
        (1, "胜利"),
        (2, "失败"),
    )

    id = models.IntegerField(primary_key=True, choices=TYPE)
    honor = models.IntegerField()
    item_id = models.IntegerField()
    item_amount = models.IntegerField()
    random_items = models.TextField(help_text='id,amount,prob;')

    class Meta:
        db_table = 'arena_match_reward'
        verbose_name = '比赛奖励'
        verbose_name_plural = "比赛奖励"

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse_items(text):
            result = []
            for x in text.split(';'):
                _a, _b, _c = x.split(',')
                result.append((int(_a), int(_b), int(_c)))

        for f in fixture:
            f['fields']['random_items'] = _parse_items(f['fields']['random_items'])

        return fixture

class BuyTimesCost(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='购买次数')
    diamond = models.IntegerField()

    class Meta:
        db_table = 'arena_buy_times_cost'
        verbose_name = '购买次数消费'
        verbose_name_plural = "购买次数消费"
