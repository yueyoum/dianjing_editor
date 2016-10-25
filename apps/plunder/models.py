# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from misc import parse_text

class BaseStationLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.TextField()
    exp = models.IntegerField()

    class Meta:
        db_table = 'base_station_level'
        verbose_name = '基地等级'
        verbose_name_plural = '基地等级'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['product'] = parse_text(f['fields']['product'], 2)

        return fixture

class PlunderIncome(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='胜几路')
    percent = models.IntegerField()
    exp = models.IntegerField()
    extra_income = models.TextField()

    class Meta:
        db_table = 'plunder_income'
        verbose_name = '掠夺收益'
        verbose_name_plural = '掠夺收益'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            extra_income = parse_text(f['fields']['extra_income'], 3)

            for i in range(1, len(extra_income)):
                extra_income[i][2] += extra_income[i-1][2]

            f['fields']['extra_income'] = extra_income

        return fixture

class PlunderBuyTimesCost(models.Model):
    id = models.IntegerField(primary_key=True)
    cost = models.IntegerField()

    class Meta:
        db_table = 'plunder_buy_times_cost'
        verbose_name = '掠夺购买次数花费'
        verbose_name_plural = '掠夺购买次数花费'

class PlunderNPC(models.Model):
    id = models.IntegerField(primary_key=True)
    level_low = models.IntegerField()
    level_high = models.IntegerField()
    way_one = models.CommaSeparatedIntegerField(max_length=255)
    way_two = models.CommaSeparatedIntegerField(max_length=255)
    way_three = models.CommaSeparatedIntegerField(max_length=255)

    class Meta:
        db_table = 'plunder_npc'
        verbose_name = '掠夺NPC'
        verbose_name_plural = '掠夺NPC'

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse(text):
            result = []
            for i in text.split(','):
                if not i:
                    continue

                result.append(int(i))

            return result

        for f in fixture:
            f['fields']['way_one'] = _parse(f['fields']['way_one'])
            f['fields']['way_two'] = _parse(f['fields']['way_two'])
            f['fields']['way_three'] = _parse(f['fields']['way_three'])

        return fixture


class PlunderDayReward(models.Model):
    id = models.IntegerField(primary_key=True)
    reward = models.TextField()

    class Meta:
        db_table = 'plunder_day_reward'
        verbose_name = '掠夺每日奖励'
        verbose_name_plural = '掠夺每日奖励'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['reward'] = parse_text(f['fields']['reward'], 2)

        return fixture