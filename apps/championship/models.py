# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from misc import parse_text


class ChampionshipWinScore(models.Model):
    id = models.IntegerField(primary_key=True)
    score = models.IntegerField()

    class Meta:
        db_table = 'championship_winscore'
        verbose_name = '获取分数'
        verbose_name_plural = '获取分数'


class ChampionshipScoreReward(models.Model):
    id = models.IntegerField(primary_key=True)
    mail_title = models.CharField(max_length=255)
    mail_content = models.TextField()
    reward = models.TextField()

    class Meta:
        db_table = 'championship_score_reward'
        verbose_name = '小组分数奖励'
        verbose_name_plural = '小组分数奖励'

    @classmethod
    def patch_fixture(cls, fixtures):
        for f in fixtures:
            f['fields']['reward'] = parse_text(f['fields']['reward'], 2)

        return fixtures


class ChampionshipRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    mail_title = models.CharField(max_length=255)
    mail_content = models.TextField()
    reward = models.TextField()

    class Meta:
        db_table = 'championship_rank_reward'
        verbose_name = '小组排名奖励'
        verbose_name_plural = '小组排名奖励'

    @classmethod
    def patch_fixture(cls, fixtures):
        for f in fixtures:
            f['fields']['reward'] = parse_text(f['fields']['reward'], 2)

        return fixtures


class ChampionshipBet(models.Model):
    ROUND = (
        (16, '16 进 8'),
        (8, '8 进 4'),
        (4, '4 进 2'),
        (2, '2 进 1'),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    round_num = models.IntegerField(choices=ROUND)

    cost = models.TextField()

    win_mail_title = models.CharField(max_length=255)
    win_mail_content = models.TextField()
    win_reward = models.TextField()

    lose_mail_title = models.CharField(max_length=255)
    lose_mail_content = models.TextField()
    lose_reward = models.TextField()

    class Meta:
        db_table = 'championship_bet'
        verbose_name = '下注'
        verbose_name_plural = '下注'

    @classmethod
    def patch_fixture(cls, fixtures):
        for f in fixtures:
            f['fields']['cost'] = parse_text(f['fields']['cost'], 2)
            f['fields']['win_reward'] = parse_text(f['fields']['win_reward'], 2)
            f['fields']['lose_reward'] = parse_text(f['fields']['lose_reward'], 2)

        return fixtures
