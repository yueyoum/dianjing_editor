# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UnionLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    contribution = models.IntegerField()
    members_limit = models.IntegerField()

    class Meta:
        db_table = 'union_level'
        verbose_name = '公会等级'
        verbose_name_plural = '公会等级'


class UnionSignIn(models.Model):
    id = models.IntegerField(primary_key=True)
    contribution = models.IntegerField()
    rewards = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    vip = models.IntegerField()

    class Meta:
        db_table = 'union_singin'
        verbose_name = '公会签到'
        verbose_name_plural = '公会签到'

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse(text):
            result = []
            for x in text.split(';'):
                if not x:
                    continue

                a, b = x.split(',')
                result.append((int(a), int(b)))

            return result

        for f in fixture:
            f['fields']['rewards'] = _parse(f['fields']['rewards'])
            f['fields']['cost'] = _parse(f['fields']['cost'])

        return fixture
