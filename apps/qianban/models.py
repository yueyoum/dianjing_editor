# -*- coding: utf-8 -*-

from django.db import models

class QianBan(models.Model):
    CONDITION_TYPE = (
        (1, "装配兵种"),
        (2, "选手同时上阵")
    )

    id = models.IntegerField(primary_key=True)
    staff_oid = models.IntegerField()
    name = models.CharField(max_length=32, verbose_name="名字")
    des = models.TextField(verbose_name="描述")
    story_des = models.TextField(blank=True, verbose_name="背景故事")

    condition_tp = models.IntegerField(choices=CONDITION_TYPE, verbose_name="条件")
    condition_value = models.CommaSeparatedIntegerField(max_length=255, verbose_name="条件值",
                                                        help_text='id,id,id'
                                                        )

    talent_effect_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'qianban'
        verbose_name = '牵绊'
        verbose_name_plural = "牵绊"


    @classmethod
    def patch_fixture(cls, fixture):
        def _parse_value(value):
            result = []
            for i in value.split(','):
                if not i:
                    continue

                result.append(int(i))

            return result

        data = {}
        for f in fixture:
            f['fields']['condition_value'] = _parse_value(f['fields']['condition_value'])
            staff_oid = f['fields'].pop('staff_oid')

            if staff_oid in data:
                data[staff_oid][f['pk']] = f['fields']
            else:
                data[staff_oid] = {f['pk']: f['fields']}

        new_fixture = []
        for k, v in data.iteritems():
            f = {
                'pk': k,
                'fields': {
                    'info': v
                }
            }

            new_fixture.append(f)

        return new_fixture


# 助威
class Inspire(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='孔位ID')
    challenge_id = models.IntegerField(verbose_name='开启需要通过关卡')
    des = models.TextField()

    class Meta:
        db_table = 'inspire'
        verbose_name = '助威'
        verbose_name_plural = '助威'


class InspireLevelAddition(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.TextField()

    attack = models.IntegerField()
    attack_percent = models.FloatField()

    defense = models.IntegerField()
    defense_percent = models.FloatField()

    manage = models.IntegerField()
    manage_percent = models.FloatField()

    operation = models.IntegerField()
    operation_percent = models.FloatField()

    class Meta:
        db_table = 'inspire_level_addition'
        verbose_name = '助威等级加成'
        verbose_name_plural = '助威等级加成'


class InspireStepAddition(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.TextField()

    attack_percent = models.FloatField(verbose_name='攻击百分比')
    defense_percent = models.FloatField(verbose_name='防御百分比')
    hp_percent = models.FloatField(verbose_name='生命百分比')

    hit_rate = models.FloatField(verbose_name='命中率')
    dodge_rate = models.FloatField(verbose_name='闪避率')
    crit_rate = models.FloatField(verbose_name='暴击率')
    toughness_rate = models.FloatField(verbose_name='韧性')
    crit_multiple = models.FloatField(verbose_name='暴击被率')

    hurt_addition_to_terran = models.FloatField(verbose_name='对人族伤害加成')
    hurt_addition_to_protoss = models.FloatField(verbose_name='对神族伤害加成')
    hurt_addition_to_zerg = models.FloatField(verbose_name='对虫族伤害加成')

    hurt_addition_by_terran = models.FloatField(verbose_name='受到人族伤害加成')
    hurt_addition_by_protoss = models.FloatField(verbose_name='受到神族伤害加成')
    hurt_addition_by_zerg = models.FloatField(verbose_name='受到虫族伤害加成')


    class Meta:
        db_table = 'inspire_step_addition'
        verbose_name = '助威等阶加成'
        verbose_name_plural = '助威等阶加成'