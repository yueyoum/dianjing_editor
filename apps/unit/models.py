# -*- coding: utf-8 -*-

from django.db import models


class UnitNew(models.Model):
    TP = (
        (1, '地面单位'),
        (2, '空中单位'),
    )

    ATTACK_TP = (
        (1, '物理攻击'),
        (2, '能量攻击'),
        (3, '爆炸攻击'),
    )

    DEFENSE_TP = (
        (1, '生物护甲'),
        (2, '能量护甲'),
        (3, '机械护甲'),
    )

    RANGE_TP = (
        (1, '近战'),
        (2, '远程'),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="名字")
    model = models.CharField(max_length=255, verbose_name="模型")
    icon = models.CharField(max_length=255, verbose_name="图标")
    tp = models.IntegerField(choices=TP, default=1, verbose_name="类型")
    race = models.ForeignKey('staff.StaffRace', verbose_name="种族")

    attack_tp = models.IntegerField(choices=ATTACK_TP, verbose_name='攻击类型')
    defense_tp = models.IntegerField(choices=DEFENSE_TP, verbose_name='防御类型')
    range_tp = models.IntegerField(choices=RANGE_TP, verbose_name='范围类型')

    operation = models.IntegerField(verbose_name='操作')
    skill_1 = models.IntegerField()
    skill_2 = models.IntegerField()

    hp_max_base = models.IntegerField(verbose_name='基础最大生命值')
    attack_base = models.IntegerField(verbose_name='基础攻击')
    defense_base = models.IntegerField(verbose_name='基础防御')

    attack_speed_base = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='基础攻击速度')
    attack_range_base = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='基础攻击射程')
    move_speed_base = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='基础移动速度')

    hit_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='命中率')
    dodge_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='闪避率')
    crit_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='暴击率')
    toughness_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='韧性')
    crit_multiple = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='暴击被率')

    hurt_addition_to_terran = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对人族伤害加成')
    hurt_addition_to_protoss = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对神族伤害加成')
    hurt_addition_to_zerg = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对虫族伤害加成')

    hurt_addition_by_terran = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到人族伤害加成')
    hurt_addition_by_protoss = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到神族伤害加成')
    hurt_addition_by_zerg = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到虫族伤害加成')

    final_hurt_addition = models.IntegerField(verbose_name='最终伤害加成')
    final_hurt_reduce = models.IntegerField(verbose_name='最终伤害减免')

    effect_skill_1 = models.CharField(max_length=255, verbose_name='普攻动作特效')
    effect_skill_2 = models.CharField(max_length=255, verbose_name='技能动作特效')
    effect_move = models.CharField(max_length=255, verbose_name='移动特效')
    effect_die = models.CharField(max_length=255, verbose_name='死亡特效')

    class Meta:
        db_table = 'unit_new'
        verbose_name = "兵种（新）"
        verbose_name_plural = "兵种（新）"

    @classmethod
    def get_fixture_key(cls):
        return 'unit.UnitNew'

    @classmethod
    def patch_fixture(cls, fixtures):
        def parse_item_need(item_text):
            if not item_text:
                return []

            data = []
            for group in item_text.split(';'):
                _id, _amount = group.split(',')
                data.append((int(_id), int(_amount)))

            return data


        decimal_fields = []
        for _fields in cls._meta.get_fields():
            if _fields.get_internal_type() == 'DecimalField':
                decimal_fields.append(_fields.column)

        for f in fixtures:
            for field in decimal_fields:
                value = f['fields'][field]
                f['fields'][field] = float(value)


            levels = UnitLevel.objects.filter(unit_id=f['pk'])
            """:type: list[UnitLevel]"""

            levels_data = {}
            for lv in levels:
                levels_data[lv.unit_level] = {
                    'hp': lv.hp,
                    'attack': lv.attack,
                    'defense': lv.defense,
                    'update_item_need': parse_item_need(lv.update_item_need)
                }

            f['fields']['levels'] = levels_data
            if levels_data:
                f['fields']['max_level'] = max(levels_data.keys())
            else:
                f['fields']['max_level'] = 0


            steps = UnitStep.objects.filter(unit_id=f['pk'])
            """:type: list[UnitStep]"""

            steps_data = {}
            for st in steps:
                steps_data[st.unit_step] = {
                    'level_limit': st.level_limit,
                    'update_item_need': parse_item_need(st.update_item_need),
                    'hp_percent': float(st.hp_percent),
                    'attack_percent': float(st.attack_percent),
                    'defense_percent': float(st.defense_percent),
                    'hit_rate': float(st.hit_rate),
                    'dodge_rate': float(st.dodge_rate),
                    'crit_rate': float(st.crit_rate),
                    'toughness_rate': float(st.toughness_rate),
                    'crit_multiple': float(st.crit_multiple),
                    'hurt_addition_to_terran': float(st.hurt_addition_to_terran),
                    'hurt_addition_to_protoss': float(st.hurt_addition_to_protoss),
                    'hurt_addition_to_zerg': float(st.hurt_addition_to_zerg),
                    'hurt_addition_by_terran': float(st.hurt_addition_by_terran),
                    'hurt_addition_by_protoss': float(st.hurt_addition_by_protoss),
                    'hurt_addition_by_zerg': float(st.hurt_addition_by_zerg),
                }

            f['fields']['steps'] = steps_data
            if steps_data:
                f['fields']['max_step'] = max(steps_data.keys())
            else:
                f['fields']['max_step'] = 0

        return fixtures


class UnitUnLock(models.Model):
    id = models.IntegerField(primary_key=True)
    need_club_level = models.IntegerField(default=0, verbose_name='解锁所需俱乐部等级')
    need_unit_level = models.CharField(max_length=255, blank=True, verbose_name='解锁所需兵种等级',
                                         help_text='id,level;ld,level'
                                         )

    class Meta:
        db_table = 'unit_unlock'
        verbose_name = "兵种解锁"
        verbose_name_plural = "兵种解锁"

    @classmethod
    def get_fixture_key(cls):
        return 'unit.UnitUnLock'


    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            if f['fields']['need_unit_level']:
                need_unit_level = []
                for x in f['fields']['need_unit_level'].split(';'):
                    _id, _lv = x.split(',')
                    need_unit_level.append((int(_id), int(_lv)))
            else:
                need_unit_level = []

            f['fields']['need_unit_level'] = need_unit_level

        return fixture


class UnitLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    unit_id = models.IntegerField(db_index=True, verbose_name='兵种ID')
    unit_level = models.IntegerField(verbose_name='等级')
    update_item_need = models.CharField(max_length=255, blank=True, verbose_name='升到下一级所需道具',
                                        help_text='id,数量;id,数量...')

    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()

    class Meta:
        db_table = 'unit_level'
        verbose_name = "兵种升级"
        verbose_name_plural = "兵种升级"


class UnitStep(models.Model):
    id = models.IntegerField(primary_key=True)
    unit_id = models.IntegerField(db_index=True, verbose_name='兵种ID')
    unit_step = models.IntegerField(verbose_name='阶')

    level_limit = models.IntegerField(verbose_name="等级限制")
    update_item_need = models.CharField(max_length=255, blank=True, verbose_name='升到下一阶所需道具',
                                        help_text='id,数量;id,数量...')

    hp_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='生命百分比')
    attack_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='攻击百分比')
    defense_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='防御百分比')

    hit_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='命中率')
    dodge_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='闪避率')
    crit_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='暴击率')
    toughness_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='韧性')
    crit_multiple = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='暴击被率')

    hurt_addition_to_terran = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对人族伤害加成')
    hurt_addition_to_protoss = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对神族伤害加成')
    hurt_addition_to_zerg = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对虫族伤害加成')

    hurt_addition_by_terran = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到人族伤害加成')
    hurt_addition_by_protoss = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到神族伤害加成')
    hurt_addition_by_zerg = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到虫族伤害加成')


    class Meta:
        db_table = 'unit_step'
        verbose_name = "兵种升阶"
        verbose_name_plural = "兵种升阶"



class _Fixture(object):
    def __init__(self, model_name, key):
        self.race = {}
        self.model = model_name
        self.key = key

    def make_data(self, f):
        return {
            self.key: f['fields'][self.key],
            'hp_percent': float(f['fields']['hp_percent']),
            'attack_percent': float(f['fields']['attack_percent']),
            'defense_percent': float(f['fields']['defense_percent']),
            'hit_rate': float(f['fields']['hit_rate']),
            'dodge_rate': float(f['fields']['dodge_rate']),
            'crit_rate': float(f['fields']['crit_rate']),
            'toughness_rate': float(f['fields']['toughness_rate']),
            'crit_multiple': float(f['fields']['crit_multiple']),
            'hurt_addition_to_terran': float(f['fields']['hurt_addition_to_terran']),
            'hurt_addition_to_protoss': float(f['fields']['hurt_addition_to_protoss']),
            'hurt_addition_to_zerg': float(f['fields']['hurt_addition_to_zerg']),
            'hurt_addition_by_terran': float(f['fields']['hurt_addition_by_terran']),
            'hurt_addition_by_protoss': float(f['fields']['hurt_addition_by_protoss']),
            'hurt_addition_by_zerg': float(f['fields']['hurt_addition_by_zerg']),
        }

    def add(self, f):
        race = f['fields']['race']
        value = f['fields'][self.key]

        if race in self.race:
            if value in self.race[race]:
                raise ValueError()
            else:
                self.race[race].append(self.make_data(f))
        else:
            self.race[race] = [self.make_data(f)]

    def to_fixture(self):
        fixtures = []
        for k, v in self.race.iteritems():
            v.sort(key=lambda item: item[self.key])
            
            fixture = {}
            fixture['pk'] = k
            fixture['model'] = self.model
            fixture['fields'] = {
                'addition': v
            }

            fixtures.append(fixture)

        return fixtures


class UnitLevelAddition(models.Model):
    id = models.IntegerField(primary_key=True)
    race = models.IntegerField()
    level = models.IntegerField(verbose_name='等级总和')

    hp_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='生命百分比')
    attack_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='攻击百分比')
    defense_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='防御百分比')

    hit_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='命中率')
    dodge_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='闪避率')
    crit_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='暴击率')
    toughness_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='韧性')
    crit_multiple = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='暴击被率')

    hurt_addition_to_terran = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对人族伤害加成')
    hurt_addition_to_protoss = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对神族伤害加成')
    hurt_addition_to_zerg = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对虫族伤害加成')

    hurt_addition_by_terran = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到人族伤害加成')
    hurt_addition_by_protoss = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到神族伤害加成')
    hurt_addition_by_zerg = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到虫族伤害加成')


    class Meta:
        db_table = 'unit_level_addition'
        verbose_name = "种族等级加成"
        verbose_name_plural = "种族等级加成"

    @classmethod
    def get_fixture_key(cls):
        return 'unit.UnitLevelAddition'

    @classmethod
    def patch_fixture(cls, fixture):
        f = _Fixture('unit.unitleveladdition', 'level')
        for _f in fixture:
            f.add(_f)

        return f.to_fixture()


class UnitStepAddition(models.Model):
    id = models.IntegerField(primary_key=True)
    race = models.IntegerField()
    step = models.IntegerField(verbose_name='等级总和')

    hp_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='生命百分比')
    attack_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='攻击百分比')
    defense_percent = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='防御百分比')

    hit_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='命中率')
    dodge_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='闪避率')
    crit_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='暴击率')
    toughness_rate = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='韧性')
    crit_multiple = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='暴击被率')

    hurt_addition_to_terran = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对人族伤害加成')
    hurt_addition_to_protoss = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对神族伤害加成')
    hurt_addition_to_zerg = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='对虫族伤害加成')

    hurt_addition_by_terran = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到人族伤害加成')
    hurt_addition_by_protoss = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到神族伤害加成')
    hurt_addition_by_zerg = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='受到虫族伤害加成')


    class Meta:
        db_table = 'unit_step_addition'
        verbose_name = "种族品阶加成"
        verbose_name_plural = "种族品阶加成"

    @classmethod
    def get_fixture_key(cls):
        return 'unit.UnitStepAddition'

    @classmethod
    def patch_fixture(cls, fixture):
        f = _Fixture('unit.unitstepaddition', 'step')
        for _f in fixture:
            f.add(_f)

        return f.to_fixture()