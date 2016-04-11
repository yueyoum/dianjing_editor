# -*- coding: utf-8 -*-

from django.db import models

class Buff(models.Model):
    id = models.IntegerField(primary_key=True)
    tp = models.IntegerField()
    level = models.IntegerField()
    effect = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        db_table = 'buff'
        verbose_name = 'Buff'
        verbose_name_plural = 'Buff'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['value'] = float(f['fields']['value'])

        return fixture


class TalentSkill(models.Model):
    TARGET = (
        (1, '选手自身'),
        (2, '上阵所有选手'),
        (3, '上阵所有人族选手'),
        (4, '上阵所有虫族选手'),
        (5, '上阵所有神族选手'),
        (6, '选手自身携带的任意兵种'),
        (7, '选手自身携带的人族兵种'),
        (8, '选手自身携带的虫族兵种'),
        (9, '选手自身携带的神族兵种'),
        (10, '上阵所有选手携带的任意兵种'),
        (11, '上阵所有选手携带的人族兵种'),
        (12, '上阵所有选手携带的虫族兵种'),
        (13, '上阵所有选手携带的神族兵种'),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    des = models.TextField()
    target = models.IntegerField(choices=TARGET)

    staff_attack = models.IntegerField()
    staff_attack_percent = models.DecimalField(max_digits=8, decimal_places=4)

    staff_defense = models.IntegerField()
    staff_defense_percent = models.DecimalField(max_digits=8, decimal_places=4)

    staff_manage = models.IntegerField()
    staff_manage_percent = models.DecimalField(max_digits=8, decimal_places=4)

    staff_operation = models.IntegerField()
    staff_operation_percent = models.DecimalField(max_digits=8, decimal_places=4)

    unit_hp_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='生命百分比')
    unit_attack_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='攻击百分比')
    unit_defense_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='防御百分比')

    unit_hit_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='命中率')
    unit_dodge_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='闪避率')
    unit_crit_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='暴击率')
    unit_toughness_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='韧性')
    unit_crit_multiple = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='暴击被率')

    unit_hurt_addition_to_terran = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对人族伤害加成')
    unit_hurt_addition_to_protoss = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对神族伤害加成')
    unit_hurt_addition_to_zerg = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对虫族伤害加成')

    unit_hurt_addition_by_terran = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到人族伤害加成')
    unit_hurt_addition_by_protoss = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到神族伤害加成')
    unit_hurt_addition_by_zerg = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到虫族伤害加成')

    unit_final_hurt_addition = models.IntegerField(verbose_name='最终伤害加成')
    unit_final_hurt_reduce = models.IntegerField(verbose_name='最终伤害减免')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'talent_skill'
        verbose_name = '天赋'
        verbose_name_plural = '天赋'

    @classmethod
    def patch_fixture(cls, fixture):
        decimal_fields = []
        for _fields in cls._meta.get_fields():
            if _fields.get_internal_type() == 'DecimalField':
                decimal_fields.append(_fields.column)

        for f in fixture:
            for field in decimal_fields:
                value = f['fields'][field]
                f['fields'][field] = float(value)

        return fixture