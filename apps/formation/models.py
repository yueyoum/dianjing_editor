# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Slot(models.Model):
    id = models.IntegerField(primary_key=True)
    club_level = models.IntegerField()
    des = models.TextField()

    class Meta:
        db_table = 'formation_slot'
        verbose_name = '阵型格子'
        verbose_name_plural = '阵型格子'


class Formation(models.Model):
    TP = (
        (0, '通用'),
        (1, '人'),
        (2, '神'),
        (3, '虫'),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    des = models.TextField()
    tp = models.IntegerField(choices=TP)
    active_need_star = models.IntegerField()
    active_need_items = models.CharField(max_length=255, help_text='id,amount;id,amount...')
    use_condition = models.CharField(max_length=255)

    class Meta:
        db_table = 'formation'
        verbose_name = '阵型'
        verbose_name_plural = '阵型'

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse_items(text):
            if not text:
                return []

            result = []
            for x in text.split(';'):
                if not x:
                    continue
                a, b = x.split(',')
                result.append((int(a), int(b)))

            return result


        for f in fixture:
            f['fields']['active_need_items'] = _parse_items(f['fields']['active_need_items'])
            f['fields']['use_condition'] = [int(i) for i in f['fields']['use_condition'].split(',')]

            levels = {}
            for lv in FormationLevel.objects.filter(formation_id=f['pk']):
                levels[lv.level] = {
                    'level_up_need_star': lv.level_up_need_star,
                    'level_up_need_items': _parse_items(lv.level_up_need_items),
                    'talent_effects': [int(i) for i in lv.talent_effects.split(';')],
                    'side_attack_amount': lv.side_attack_amount,
                }

            f['fields']['levels'] = levels
            f['fields']['max_level'] = max(levels.keys())

        return fixture

class FormationLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    formation_id = models.IntegerField(db_index=True)
    level = models.IntegerField()
    level_up_need_star = models.IntegerField()
    level_up_need_items = models.CharField(max_length=255)
    talent_effects = models.CharField(max_length=255)

    side_attack_amount = models.IntegerField()

    class Meta:
        db_table = 'formation_level'
        verbose_name = '阵型等级'
        verbose_name_plural = '阵型等级'