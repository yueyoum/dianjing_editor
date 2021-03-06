# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ArenaNPC(models.Model):
    id = models.IntegerField(primary_key=True)
    score_low = models.IntegerField(default=1000)
    score_high = models.IntegerField(default=1000)
    npcs = models.CommaSeparatedIntegerField(max_length=255)
    amount = models.IntegerField(default=0)

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
    des = models.CharField(max_length=255, blank=True)

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

            return result

        for f in fixture:
            f['fields']['reward'] = _parse_reward(f['fields']['reward'])

        return fixture


class RankReward(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='排名上限')
    rank_des = models.CharField(blank=True, max_length=255)
    reward = models.CharField(max_length=255, help_text='id,amount;id,amount')
    mail_title = models.CharField(max_length=255)
    mail_content = models.CharField(max_length=255)

    class Meta:
        db_table = 'arena_rank_reward'
        verbose_name = '排名奖励 - 日'
        verbose_name_plural = "排名奖励 - 日"

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse_reward(text):
            result = []
            for x in text.split(';'):
                _a, _b = x.split(',')
                result.append((int(_a), int(_b)))

            return result

        for f in fixture:
            f['fields']['reward'] = _parse_reward(f['fields']['reward'])

        return fixture

class RankRewardWeekly(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='排名上限')
    rank_des = models.CharField(blank=True, max_length=255)
    reward = models.CharField(max_length=255, help_text='id,amount;id,amount')
    mail_title = models.CharField(max_length=255)
    mail_content = models.CharField(max_length=255)

    class Meta:
        db_table = 'arena_rank_reward_weekly'
        verbose_name = '排名奖励 - 周'
        verbose_name_plural = "排名奖励 - 周"

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse_reward(text):
            result = []
            for x in text.split(';'):
                _a, _b = x.split(',')
                result.append((int(_a), int(_b)))

            return result

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
    random_items = models.TextField(blank=True, help_text='id,amount,prob;')

    class Meta:
        db_table = 'arena_match_reward'
        verbose_name = '比赛奖励'
        verbose_name_plural = "比赛奖励"

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse_items(text):
            if not text:
                return []

            result = []
            for x in text.split(';'):
                _a, _b, _c = x.split(',')
                result.append([int(_a), int(_b), int(_c)])

            for i in range(1, len(result)-1):
                result[i][2] += result[i-1][2]

            return result

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


class MatchLogTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    template = models.TextField()

    class Meta:
        db_table = 'arena_match_log_template'
        verbose_name = '战报模板'
        verbose_name_plural = '战报模板'


class SearchRange(models.Model):
    id = models.IntegerField(primary_key=True)
    range_1 = models.FloatField()
    range_2 = models.FloatField()

    score_win = models.IntegerField(default=0)
    score_lose = models.IntegerField(default=0)

    class Meta:
        db_table = 'arena_search_range'
        verbose_name = '对手搜索范围'
        verbose_name_plural = '对手搜索范围'


class ResetCost(models.Model):
    id = models.IntegerField(primary_key=True)
    diamond = models.IntegerField()

    class Meta:
        db_table = 'arena_reset_cost'
        verbose_name = '重置花费'
        verbose_name_plural = '重置花费'
