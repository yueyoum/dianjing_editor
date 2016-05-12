# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class TerritoryBuilding(models.Model):
    id = models.IntegerField(primary_key=True)
    building_id = models.IntegerField()
    building_name = models.CharField(max_length=32)
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

            return [int(i) for i in text.split(';') if i]

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
            name = ""
            levels = {}
            for i in v:
                name = i.pop('building_name')
                lv = i.pop('building_level')

                levels[lv] = i

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
                        'cost_amount': [int(x) for x in ep.cost_amount.split(';') if x]
                    }

                slots_data[s.id]['building_levels'] = slot_building_levels

            data = {
                'pk': k,
                'fields': {
                    'name': name,
                    'levels': levels,
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

    class Meta:
        db_table = 'territory_building_slot_extra_product'
        verbose_name = '格子产出'
        verbose_name_plural = '格子产出'


class StaffSpecialProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    product_1 = models.TextField(help_text='id,amount_low,amount_high;')
    product_2 = models.TextField(help_text='id,amount_low,amount_high;')
    product_3 = models.TextField(help_text='id,amount_low,amount_high;')

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
            f['fields']['product_1'] = _parse(f['fields']['product_1'])
            f['fields']['product_2'] = _parse(f['fields']['product_2'])
            f['fields']['product_3'] = _parse(f['fields']['product_3'])

        return fixture