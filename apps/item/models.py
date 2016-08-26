# -*- coding: utf-8 -*-

from django.db import models
from misc import parse_text

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
    sub_tp = models.IntegerField(default=0)
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
        (5, '特殊'),
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
                if not group_text:
                    continue
                    
                group_data = []

                for item_text in group_text.split(';'):
                    if not item_text:
                        continue

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

    @classmethod
    def get_fixture_key(cls):
        return 'item.ItemMerge'


class ItemExp(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'item_exp'


def _parse_common_split_text(text):
    if not text:
        return []

    result = []
    for x in text.split(','):
        if not x:
            continue

        result.append(int(x))

    return result


class EquipmentSpecial(models.Model):
    id = models.IntegerField(primary_key=True)

    staff_attack = models.IntegerField()
    staff_defense = models.IntegerField()
    staff_manage = models.IntegerField()

    staff_attack_percent = models.FloatField()
    staff_defense_percent = models.FloatField()
    staff_manage_percent = models.FloatField()

    unit_attack_percent = models.FloatField(verbose_name='攻击百分比')
    unit_defense_percent = models.FloatField(verbose_name='防御百分比')
    unit_hp_percent = models.FloatField(verbose_name='生命百分比')

    unit_hit_rate = models.FloatField(verbose_name='命中率')
    unit_dodge_rate = models.FloatField(verbose_name='闪避率')
    unit_crit_rate = models.FloatField(verbose_name='暴击率')
    unit_toughness_rate = models.FloatField(verbose_name='韧性')
    unit_crit_multiple = models.FloatField(verbose_name='暴击被率')

    unit_hurt_addition_to_terran = models.FloatField(verbose_name='对人族伤害加成')
    unit_hurt_addition_to_protoss = models.FloatField(verbose_name='对神族伤害加成')
    unit_hurt_addition_to_zerg = models.FloatField(verbose_name='对虫族伤害加成')

    unit_hurt_addition_by_terran = models.FloatField(verbose_name='受到人族伤害加成')
    unit_hurt_addition_by_protoss = models.FloatField(verbose_name='受到神族伤害加成')
    unit_hurt_addition_by_zerg = models.FloatField(verbose_name='受到虫族伤害加成')

    skills = models.CharField(max_length=255)

    class Meta:
        db_table = 'equipment_special'
        verbose_name = '特殊装备'
        verbose_name_plural = '特殊装备'


    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['skills'] = _parse_common_split_text(f['fields']['skills'])

        return fixture


class EquipmentSpecialGrowingProperty(models.Model):
    id = models.IntegerField(primary_key=True)
    growing_low = models.IntegerField()
    growing_high = models.IntegerField()
    property_active_levels = models.CharField(max_length=255, blank=True)
    skill_active_levels = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'equipment_special_growing_property'
        verbose_name = '特殊装备成长率属性'
        verbose_name_plural = '特殊装备成长率属性'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['property_active_levels'] = _parse_common_split_text(f['fields']['property_active_levels'])
            f['fields']['skill_active_levels'] = _parse_common_split_text(f['fields']['skill_active_levels'])

        return fixture


class EquipmentSpecialGenerate(models.Model):
    id = models.IntegerField(primary_key=True)
    normal_cost = models.TextField()
    normal_generate = models.TextField()
    advance_cost = models.TextField()
    advance_generate = models.TextField()

    minutes = models.IntegerField()

    class Meta:
        db_table = 'equipment_special_generate'
        verbose_name = '特殊装备制造'
        verbose_name_plural = '特殊装备制造'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['normal_cost'] = parse_text(f['fields']['normal_cost'], 2)
            f['fields']['normal_generate'] = _parse_common_split_text(f['fields']['normal_generate'])
            f['fields']['advance_cost'] = parse_text(f['fields']['advance_cost'], 2)
            f['fields']['advance_generate'] = _parse_common_split_text(f['fields']['advance_generate'])

        return fixture

class EquipmentSpecialScoreToGrowing(models.Model):
    id = models.IntegerField(primary_key=True)
    tp = models.IntegerField()

    score_low = models.IntegerField()
    score_high = models.IntegerField()

    growing_low = models.IntegerField()
    growing_high = models.IntegerField()

    class Meta:
        db_table = 'equipment_special_score_to_growing'
        verbose_name = '特殊装备分数成长率'
        verbose_name_plural = '特殊装备分数成长率'


class EquipmentSpecialLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    items = models.TextField()

    class Meta:
        db_table = 'equipment_special_level'
        verbose_name = '特殊装备等级'
        verbose_name_plural = '特殊装备等级'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['items'] = parse_text(f['fields']['items'], 2)

        return fixture