# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


def _parse(text, n):
    if not text:
        return []

    result = []

    for x in text.split(';'):
        if not x:
            continue

        x = x.split(',')
        item = []
        for i in range(n):
            item.append(int(x[i]))

        result.append(item)

    return result


class WelfareSignIn(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    reward = models.TextField(help_text='id,amount;id,amount;')

    vip = models.IntegerField()
    vip_name = models.CharField(max_length=255)
    vip_reward = models.TextField(help_text='id,amount;id,amount;')


    class Meta:
        db_table = 'welfare_signin'
        verbose_name = '签到奖励'
        verbose_name_plural = '签到奖励'

    @classmethod
    def get_fixture_key(cls):
        return 'welfare.WelfareSignin'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['reward'] = _parse(f['fields']['reward'], 2)
            f['fields']['vip_reward'] = _parse(f['fields']['vip_reward'], 2)

        return fixture



class WelfareNewPlayer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    reward = models.TextField(help_text='id,amount;id,amount;')

    class Meta:
        db_table = 'welfare_new_player'
        verbose_name = '新手礼包'
        verbose_name_plural = '新手礼包'

    @classmethod
    def get_fixture_key(cls):
        return 'welfare.WelfareNewPlayer'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['reward'] = _parse(f['fields']['reward'], 2)

        return fixture


class WelfareLevelReward(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    reward = models.TextField(help_text='id,amount;id,amount;')

    class Meta:
        db_table = 'welfare_level_reward'
        verbose_name = '等级礼包'
        verbose_name_plural = '等级礼包'

    @classmethod
    def get_fixture_key(cls):
        return 'welfare.WelfareLevelReward'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['reward'] = _parse(f['fields']['reward'], 2)

        return fixture