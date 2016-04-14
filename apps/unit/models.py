# -*- coding: utf-8 -*-

from django.db import models

class Policy(models.Model):
    ROUND = (
        (1, "第一轮"),
        (2, "第二轮"),
        (3, "第三轮"),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="名字")
    icon = models.CharField(max_length=255, verbose_name="图标")
    advantage_add_round = models.IntegerField(choices=ROUND, verbose_name="在第几轮加成")
    advantage_add_value = models.IntegerField(verbose_name="加成数值")

    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'policy'
        verbose_name = "战术"
        verbose_name_plural = "战术"


class Unit(models.Model):
    TP = (
        (1, '地面单位'),
        (2, '空中单位'),
    )

    TARGET = (
        (0, '全部'),
        (1, '对地攻击'),
        (2, '对空攻击'),
    )

    id = models.IntegerField(primary_key=True)
    icon = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=32, verbose_name="兵种")
    race = models.ForeignKey('staff.StaffRace', verbose_name="种族")

    tp = models.IntegerField(choices=TP, default=1, verbose_name="类型")
    target = models.IntegerField(choices=TARGET, default=0, verbose_name="攻击目标")
    base_amount = models.IntegerField(default=0, verbose_name="基础数量")

    first_trig = models.IntegerField("开局触发值")
    second_trig = models.IntegerField("中间局触发值")
    third_trig = models.IntegerField("结束局触发值")
    skill = models.ForeignKey('skill.Skill', verbose_name="技能")

    trig_at = models.IntegerField(default=0, verbose_name="出兵时间")
    trig_prob = models.IntegerField(default=0, verbose_name="出兵几率")

    power = models.IntegerField(default=0, verbose_name="战斗力")
    consume_per_second = models.IntegerField(default=0, verbose_name="每秒消耗资源")
    count_per_second = models.FloatField(default=0, verbose_name="每秒暴兵效率")
    draft_total_time = models.IntegerField(default=0, verbose_name="暴兵时间")

    def __unicode__(self):
        return self.name


    class Meta:
        db_table = 'unit'
        ordering = ('id',)
        verbose_name = "单位"
        verbose_name_plural = "单位"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:

            des = {
                int(d.policy.id): [line.split('|') for line in d.des.strip('\r\n').split('\r\n')] for d in cls.objects.get(id=f['pk']).des.all()
            }

            f['fields']['des'] = des

        return fixture


class UnitDes(models.Model):
    unit = models.ForeignKey(Unit, related_name='des')
    policy = models.ForeignKey(Policy, verbose_name="战术")
    des = models.TextField(verbose_name="描述")

    class Meta:
        db_table = 'unit_des'


class UnitEffect(models.Model):
    RACE = (
        (0, "全部"),
        (1, "人族"),
        (2, "神族"),
        (3, "虫族"),
    )

    TYPE = (
        (1, "对撞"),
        (2, "单方面挨打"),
        (3, "死亡"),
        (4, "出生"),
        (5, "天赋"),
        (6, "失败"),
        (7, "员工挨打")
    )

    id = models.IntegerField(primary_key=True)
    effect = models.CharField(max_length=255)
    race = models.IntegerField(choices=RACE, verbose_name="种族")
    tp = models.IntegerField(choices=TYPE, verbose_name="类型")

    class Meta:
        db_table = 'unit_effect'
        verbose_name = "单位特效"
        verbose_name_plural = "单位特效"


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
