# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PurchaseGoods(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.TextField(blank=True)

    rmb = models.IntegerField()
    vip_exp = models.IntegerField()
    diamond = models.IntegerField()
    diamond_extra = models.IntegerField()

    class Meta:
        db_table = 'purchase_goods'
        verbose_name = '充值商品'
        verbose_name_plural = '充值商品'


class PurchaseYueka(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.TextField(blank=True)

    rmb = models.IntegerField()
    vip_exp = models.IntegerField()

    rewards = models.CharField(max_length=255)
    mail_title = models.CharField(max_length=255)
    mail_content = models.CharField(max_length=255)

    class Meta:
        db_table = 'purchase_yueka'
        verbose_name = '月卡'
        verbose_name_plural = '月卡'

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse(text):
            res = []
            for x in text.split(';'):
                if not x:
                    continue

                a, b = x.split(',')
                res.append((int(a), int(b)))

            return res

        for f in fixture:
            f['fields']['rewards'] = _parse(f['fields']['rewards'])

        return fixture