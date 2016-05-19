# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Q

class TerritoryBuilding(models.Model):
    id = models.IntegerField(primary_key=True)
    building_id = models.IntegerField()
    building_level = models.IntegerField()

    exp = models.IntegerField()
    product_rate = models.IntegerField(verbose_name='每小时产量')
    events = models.CharField(max_length=255)
    product_limit = models.IntegerField(verbose_name='资源上限')

    class Meta:
        db_table = 'territory_building'
        verbose_name = '领地建筑'
        verbose_name_plural = '领地建筑'

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse_events(text):
            if not text:
                return []

            return [int(i) for i in text.split(',') if i]

        def _parse_extra_product(text):
            if not text:
                return []

            results = []
            for x in text.split(';'):
                if not x:
                    continue

                _id, _amount = x.split(',')
                results.append((int(_id), int(_amount)))

            return results

        buildings = {}
        for f in fixture:
            f['fields']['events'] = _parse_events(f['fields']['events'])

            bid = f['fields'].pop('building_id')
            if bid in buildings:
                buildings[bid].append(f['fields'])
            else:
                buildings[bid] = [f['fields']]

        new_fixture = []
        for k, v in buildings.iteritems():
            levels = {}
            for i in v:
                lv = i.pop('building_level')

                levels[lv] = i
                inspire = Inspire.objects.get(Q(building_id=k) & Q(building_level=lv))
                levels[lv]['inspire'] = {
                    'exp': inspire.exp,
                    'max_times': inspire.max_times,
                    'reward': inspire.parsed_reward(),
                }

            slots = BuildingSlot.objects.filter(building_id=k)
            slots_data = {}
            for s in slots:
                slots_data[s.id] = {
                    'need_building_level': s.need_building_level,
                    'need_vip_level': s.need_vip_level,
                    'exp_modulus': s.exp_modulus,
                }

                extra_products = BuildingSlotExtraProduct.objects.filter(slot_id=s.id).order_by('building_level')
                slot_building_levels = {}
                for ep in extra_products:
                    slot_building_levels[ep.building_level] = {
                        'extra_product': _parse_extra_product(ep.extra_product),
                        'cost_amount': [int(x) for x in ep.cost_amount.split(';') if x],
                        'des': ep.des
                    }

                slots_data[s.id]['building_levels'] = slot_building_levels

            data = {
                'pk': k,
                'fields': {
                    'levels': levels,
                    'max_level': max(levels.keys()),
                    'slots': slots_data,
                }
            }

            new_fixture.append(data)

        return new_fixture


class BuildingSlot(models.Model):
    id = models.IntegerField(primary_key=True)
    building_id = models.IntegerField(db_index=True)
    need_building_level = models.IntegerField()
    need_vip_level = models.IntegerField()

    exp_modulus = models.FloatField()

    class Meta:
        db_table = 'territory_building_slot'
        verbose_name = '建筑格子'
        verbose_name_plural = '建筑格子'


class BuildingSlotExtraProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    slot_id = models.IntegerField(db_index=True)
    building_level = models.IntegerField()
    extra_product = models.TextField(help_text='id,amount;')
    cost_amount = models.CharField(max_length=255)
    des = models.TextField(blank=True)

    class Meta:
        db_table = 'territory_building_slot_extra_product'
        verbose_name = '格子产出'
        verbose_name_plural = '格子产出'


class StaffSpecialProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    product_1 = models.TextField(help_text='id,amount_low,amount_high;')
    product_2 = models.TextField(help_text='id,amount_low,amount_high;')
    product_3 = models.TextField(help_text='id,amount_low,amount_high;')
    des_1 = models.TextField(blank=True)
    des_2 = models.TextField(blank=True)
    des_3 = models.TextField(blank=True)


    class Meta:
        db_table = 'territory_special_product'
        verbose_name = '选手特殊产出'
        verbose_name_plural = '选手特殊产出'

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse(text):
            result = []
            for i in text.split(';'):
                a, b, c = i.split(',')
                result.append((int(a), int(b), int(c)))

            return result

        for f in fixture:
            p1 = f['fields'].pop('product_1')
            p2 = f['fields'].pop('product_2')
            p3 = f['fields'].pop('product_3')
            d1 = f['fields'].pop('des_1')
            d2 = f['fields'].pop('des_2')
            d3 = f['fields'].pop('des_3')

            f['fields']['product'] = [_parse(p1), _parse(p2), _parse(p3)]
            f['fields']['des'] = [d1, d2, d3]

        return fixture

class Inspire(models.Model):
    id = models.IntegerField(primary_key=True)
    building_id = models.IntegerField()
    building_level = models.IntegerField()
    exp = models.IntegerField()
    max_times = models.IntegerField()
    reward = models.TextField(help_text='id,amount,prob;  概率和为100')

    class Meta:
        db_table = 'territory_inspire'
        unique_together = (('building_id', 'building_level'),)
        verbose_name = '鼓舞'
        verbose_name_plural = '鼓舞'

    def parsed_reward(self):
        result = []
        for x in self.reward.split(';'):
            if not x:
                continue

            _id, _amount, _prob = x.split(',')
            result.append([int(_id), int(_amount), int(_prob)])

        for i in range(1, len(result)):
            result[i][2] += result[i-1][2]

        return result


class InspireCost(models.Model):
    id = models.IntegerField(primary_key=True)
    diamond = models.IntegerField()

    class Meta:
        db_table = 'territory_inspire_cost'
        verbose_name = '鼓舞花费'
        verbose_name_plural = '鼓舞花费'


class ReportTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    used_for = models.CharField(max_length=255, verbose_name='用于')
    template = models.TextField()

    class Meta:
        db_table = 'territory_report_template'
        verbose_name = '工作报告模板'
        verbose_name_plural = '工作报告模板'


class TerritoryStore(models.Model):
    TYPE = (
        (1, '普通兑换'),
        (2, '高级兑换'),
    )

    CON_ID = (
        (-1, 'VIP等级'),
        (101, '建筑等级101'),
        (102, '建筑等级102'),
        (103, '建筑等级103'),
    )

    id = models.IntegerField(primary_key=True)
    tp = models.IntegerField(choices=TYPE)
    item_id = models.IntegerField()
    item_amount = models.IntegerField()
    sequence = models.IntegerField(verbose_name='位置')

    needs = models.TextField(verbose_name='所需资源')
    condition_id = models.IntegerField(choices=CON_ID, verbose_name='条件ID')
    condition_value = models.IntegerField(default=0, verbose_name='条件值')

    max_times = models.IntegerField(verbose_name='次数限制')

    class Meta:
        db_table = 'territory_store'
        verbose_name = '商店'
        verbose_name_plural = '商店'


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
            f['fields']['needs'] = _parse(f['fields']['needs'])

        return fixture