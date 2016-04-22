# -*- coding: utf-8 -*-

from django.db import models

class ItemQuality(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=32, blank=True)
    icon = models.CharField(max_length=255, blank=True)
    background = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "item_quality"
        verbose_name = "物品品质"
        verbose_name_plural = "物品品质"


class ItemNew(models.Model):
    TYPE = (
        (1, '普通道具'),
        (2, '可使用道具'),
        (3, '代币资源'),
        (4, '装备'),
        (5, '碎片'),
        (6, '选手')
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    des = models.TextField()
    icon = models.CharField(max_length=255)
    tp = models.IntegerField(choices=TYPE)
    quality = models.IntegerField()
    stack_max = models.IntegerField(verbose_name='堆叠上限')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'item_new'
        verbose_name = '道具（新）'
        verbose_name_plural = '道具（新）'


    @classmethod
    def get_fixture_key(cls):
        return 'item.ItemNew'

class EquipmentBase(models.Model):
    TYPE = (
        (1, '鼠标'),
        (2, '键盘'),
        (3, '显示器'),
        (4, '饰品'),
    )

    id = models.IntegerField(primary_key=True)
    tp = models.IntegerField(choices=TYPE)
    renown = models.IntegerField(verbose_name='分解获得声望')

    class Meta:
        db_table = 'equipment_base'
        verbose_name = '装备基础属性'
        verbose_name_plural = '装备基础属性'

    @classmethod
    def get_fixture_key(cls):
        return 'item.EquipmentBase'

    @classmethod
    def patch_fixture(cls, fixture):
        def parse_item_need(item_text):
            if not item_text:
                return []

            data = []
            for group in item_text.split(';'):
                _id, _amount = group.split(',')
                data.append((int(_id), int(_amount)))

            return data

        for f in fixture:
            equip_id = f['pk']
            levels = EquipmentLevel.objects.filter(equip_id=equip_id)
            """:type: list[EquipmentLevel]"""

            levels_data = {}
            for lv in levels:
                levels_data[lv.equip_level] = {
                    'attack': lv.attack,
                    'attack_percent': float(lv.attack_percent),
                    'defense': lv.defense,
                    'defense_percent': float(lv.defense_percent),
                    'manage': lv.manage,
                    'manage_percent': float(lv.manage_percent),
                    'operation': lv.operation,
                    'operation_percent': float(lv.operation_percent),
                    'update_item_need': parse_item_need(lv.update_item_need)
                }

            f['fields']['levels'] = levels_data
            if levels_data:
                f['fields']['max_level'] = max(levels_data.keys())
            else:
                f['fields']['max_level'] = 0

        return fixture


class EquipmentLevel(models.Model):
    id = models.IntegerField(primary_key=True)

    equip_id = models.IntegerField(db_index=True)
    equip_level = models.IntegerField()

    attack = models.IntegerField()
    attack_percent = models.DecimalField(max_digits=8, decimal_places=4)

    defense = models.IntegerField()
    defense_percent = models.DecimalField(max_digits=8, decimal_places=4)

    manage = models.IntegerField()
    manage_percent = models.DecimalField(max_digits=8, decimal_places=4)

    operation = models.IntegerField()
    operation_percent = models.DecimalField(max_digits=8, decimal_places=4)

    update_item_need = models.CharField(max_length=255, blank=True, verbose_name='升级所需道具',
                                        help_text='id,数量;id,数量...')

    class Meta:
        db_table = 'equipment_level'
        verbose_name = '装备等级'
        verbose_name_plural = '装备等级'


class ItemUse(models.Model):
    id = models.IntegerField(primary_key=True)
    use_item_id = models.IntegerField(default=0)
    use_item_amount = models.IntegerField(default=0)

    result = models.TextField(help_text='ID1,数量,几率;ID2,数量,几率|ID11,数量,几率;ID12,数量,几率|...')

    class Meta:
        db_table = 'item_use'
        verbose_name = '道具使用'
        verbose_name_plural = '道具使用'

    @classmethod
    def patch_fixture(cls, fixture):
        def parse_result(result_text):
            result = []

            for group_text in result_text.split('|'):
                group_data = []

                for item_text in group_text.split(';'):
                    _id, _amount, _prob = item_text.split(',')
                    group_data.append(
                        (int(_id), int(_amount), int(_prob))
                    )

                result.append(group_data)

            return result

        for f in fixture:
            result = f['fields']['result']
            f['fields']['result'] = parse_result(result)

        return fixture


class ItemMerge(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField()
    to_id = models.IntegerField()
    renown = models.IntegerField(verbose_name='分解获得声望')
    crystal = models.IntegerField(verbose_name='分解获得水晶')

    class Meta:
        db_table = 'item_merge'
        verbose_name = '碎片合成'
        verbose_name_plural = '碎片合成'


class ItemExp(models.Model):
    id = models.IntegerField(primary_key=True)
    exp = models.IntegerField()

    class Meta:
        db_table = 'item_exp'
        verbose_name = '经验道具'
        verbose_name_plural = '经验道具'
