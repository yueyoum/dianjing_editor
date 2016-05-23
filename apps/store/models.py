# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class StoreCondition(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.CharField(max_length=255)

    class Meta:
        db_table = 'store_condition'
        verbose_name = '商店条件'
        verbose_name_plural = '商店条件'


class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    tp = models.IntegerField(verbose_name='类型')
    tp_name = models.CharField(max_length=255)
    club_level_min = models.IntegerField(default=0, help_text='0 表示没有限制')
    club_level_max = models.IntegerField(default=0, help_text='0 表示没有限制')

    money_id = models.IntegerField(verbose_name='显示的货币')
    refresh_hour_interval = models.IntegerField(verbose_name='自动刷新间隔小时数')
    position = models.IntegerField(verbose_name='位置')
    condition_id = models.IntegerField()
    condition_value = models.IntegerField()

    times_limit = models.IntegerField()
    content = models.TextField(help_text='售卖ID,售卖数量;需要ID,需要数量')

    class Meta:
        db_table = 'store'
        verbose_name = '商店'
        verbose_name_plural = '商店'

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse(text):
            result = []
            for x in fixture.split(';'):
                if not x:
                    continue

                a, b, c, d = x.split(',')
                result.append((
                    int(a), int(b), int(c), int(d)
                ))

            return result

        for f in fixture:
            f['fields']['content'] = _parse(f['fields']['content'])


class StoreRefresh(models.Model):
    id = models.IntegerField(primary_key=True)
    store_tp = models.IntegerField(verbose_name='商店类型')
    times = models.IntegerField(verbose_name='刷新次数')
    diamond = models.IntegerField(verbose_name='所需钻石')

    class Meta:
        db_table = 'store_refresh'
        verbose_name = '刷新花费'
        verbose_name_plural = '刷新花费'

    @classmethod
    def patch_fixture(cls, fixture):
        result = {}
        for f in fixture:
            pk = f['store_tp']
            data = [f['fields']['times'], f['fields']['diamond']]

            if pk in result:
                result[pk].append(data)
            else:
                result[pk] = [data]

        new_fixture = []
        for k, v in result.iteritems():
            v.sort(key=lambda item: -item[0])
            new_fixture.append({
                'pk': k,
                'fields': {
                    'cost': v
                }
            })

        return new_fixture

