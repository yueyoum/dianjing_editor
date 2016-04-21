# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class VIP(models.Model):
    id = models.IntegerField(primary_key=True)
    update_vip_exp = models.IntegerField()

    item_id = models.IntegerField(verbose_name='礼包ID')
    diamond_original = models.IntegerField(verbose_name='钻石原价')
    diamond_now = models.IntegerField(verbose_name='钻石现价')
    item_preview = models.TextField(verbose_name='礼包预览')

    des = models.TextField()

    class Meta:
        db_table = "vip"
        verbose_name = "VIP"
        verbose_name_plural = "VIP"

    @classmethod
    def patch_fixture(cls, fixture):
        def parse_item(item_text):
            if not item_text:
                return []

            data = []
            for group in item_text.split(';'):
                _id, _amount = group.split(',')
                data.append((int(_id), int(_amount)))

            return data

        for f in fixture:
            f['fields']['item_preview'] = parse_item(f['fields']['item_preview'])

        return fixture
