# -*- coding: utf-8 -*-

from django.db import models

class StaffRace(models.Model):
    id = models.IntegerField(primary_key=True)
    icon = models.CharField(max_length=255, blank=True)
    name = models.CharField(unique=True, max_length=32, verbose_name="名称")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'staff_race'
        verbose_name = "种族"
        verbose_name_plural = "种族"


class StaffHot(models.Model):
    id = models.IntegerField(primary_key=True)
    cost = models.IntegerField(verbose_name="花费")

    class Meta:
        db_table = "staff_hot"
        verbose_name = "员工招募-人气王"
        verbose_name_plural = "员工招募-人气王"


class StaffRecruitSettings(models.Model):
    recruit = models.ForeignKey('StaffRecruit', related_name='statff_settings')
    quality = models.IntegerField()
    first_amount = models.IntegerField(verbose_name="首次刷新出现次数")
    lucky_amount = models.IntegerField(verbose_name="幸运刷新出现次数")
    normal_amount = models.IntegerField(verbose_name="平时出现次数")

    class Meta:
        db_table = 'staff_recruit_settings'


class StaffRecruit(models.Model):
    COST_TYPE = (
        (1, "软妹币"),
        (2, "钻石")
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    cost_type = models.IntegerField(choices=COST_TYPE, verbose_name="花费类型")
    cost_value = models.IntegerField(verbose_name="花费金额")
    lucky_times = models.IntegerField(verbose_name="幸运次数")

    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'staff_recruit'
        verbose_name = "员工招募-合约"
        verbose_name_plural = "员工招募-合约"

    @classmethod
    def patch_fixture(cls, fixture):
        for s in cls.objects.all():
            staff_settings = []
            for ss in s.statff_settings.all():
                staff_settings.append({
                    'quality': ss.quality.id,
                    'first_amount': ss.first_amount,
                    'lucky_amount': ss.lucky_amount,
                    'normal_amount': ss.normal_amount
                })

            for f in fixture:
                if f['pk'] == s.id:
                    f['fields']['staff_settings'] = staff_settings

        return fixture


class StaffNew(models.Model):
    id = models.IntegerField(primary_key=True)
    race = models.IntegerField(default=1, verbose_name='种族')
    attack = models.IntegerField(verbose_name='进攻')
    attack_grow = models.IntegerField(default=1, verbose_name='进攻增长')
    defense = models.IntegerField(verbose_name='防守')
    defense_grow = models.IntegerField(default=1, verbose_name='防守增长')
    manage = models.IntegerField(verbose_name='运营')
    manage_grow = models.IntegerField(default=1, verbose_name='运营增长')
    operation = models.IntegerField(verbose_name='操作')
    operation_grow = models.IntegerField(default=1, verbose_name='操作增长')
    skill = models.IntegerField(verbose_name='技能ID')
    talent_skill = models.CommaSeparatedIntegerField(max_length=255, verbose_name='天赋ID',
                                                     help_text='id,id,id'
                                                     )

    crystal = models.IntegerField(verbose_name='分解获得水晶')

    class Meta:
        db_table = 'staff_new'
        verbose_name = "选手（新）"
        verbose_name_plural = "选手（新）"

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
            talent_skill = f['fields']['talent_skill']
            if talent_skill:
                f['fields']['talent_skill'] = [int(i) for i in talent_skill.split(',')]
            else:
                f['fields']['talent_skill'] = []

            steps = StaffStep.objects.filter(staff_id=f['pk'])
            """:type: list[StaffStep]"""

            steps_data = {}
            for step in steps:
                steps_data[step.staff_step] = {
                    'attack': step.attack,
                    'attack_percent': float(step.attack_percent),
                    'defense': step.defense,
                    'defense_percent': float(step.defense_percent),
                    'manage': step.manage,
                    'manage_percent': float(step.manage_percent),
                    'operation': step.operation,
                    'operation_percent': float(step.operation_percent),
                    'talent_skill': step.talent_skill,
                    'update_item_need': parse_item_need(step.update_item_need),
                    'level_limit': step.level_limit if step.level_limit else 0
                }

            f['fields']['steps'] = steps_data
            f['fields']['max_step'] = max(steps_data.keys())

        return fixture

class StaffLevelNew(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='等级')
    exp = models.IntegerField(verbose_name='所需经验', null=True, blank=True)

    class Meta:
        db_table = 'staff_level_new'
        ordering = ('id',)
        verbose_name = "选手等级（新）"
        verbose_name_plural = "选手等级（新）"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            if not f['fields']['exp']:
                f['fields']['exp'] = 0

        return fixture


class StaffStep(models.Model):
    id = models.IntegerField(primary_key=True)
    staff_id = models.IntegerField(db_index=True, verbose_name='选手ID')
    staff_step = models.IntegerField(verbose_name='阶')

    attack = models.IntegerField()
    attack_percent = models.DecimalField(max_digits=8, decimal_places=4)

    defense = models.IntegerField()
    defense_percent = models.DecimalField(max_digits=8, decimal_places=4)

    manage = models.IntegerField()
    manage_percent = models.DecimalField(max_digits=8, decimal_places=4)

    operation = models.IntegerField()
    operation_percent = models.DecimalField(max_digits=8, decimal_places=4)

    talent_skill = models.IntegerField()

    update_item_need = models.CharField(max_length=255, blank=True, verbose_name='升到下一阶所需道具',
                                        help_text='id,数量;id,数量...')

    level_limit = models.IntegerField(verbose_name='选手等级限制', null=True, blank=True)

    class Meta:
        db_table = 'staff_step'
        ordering = ('id',)
        verbose_name = "选手升阶（新）"
        verbose_name_plural = "选手升阶（新）"


class StaffStar(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='星级')
    exp = models.IntegerField(verbose_name='星级经验', null=True, blank=True)
    need_item_id = models.IntegerField(null=True, blank=True)
    need_item_amount = models.IntegerField(null=True, blank=True)

    attack = models.IntegerField()
    attack_percent = models.DecimalField(max_digits=8, decimal_places=4)

    defense = models.IntegerField()
    defense_percent = models.DecimalField(max_digits=8, decimal_places=4)

    manage = models.IntegerField()
    manage_percent = models.DecimalField(max_digits=8, decimal_places=4)

    operation = models.IntegerField()
    operation_percent = models.DecimalField(max_digits=8, decimal_places=4)


    class Meta:
        db_table = 'staff_star'
        ordering = ('id',)
        verbose_name = "选手升星（新）"
        verbose_name_plural = "选手升星（新）"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            if not f['fields']['exp']:
                f['fields']['exp'] = 0

            if not f['fields']['need_item_id']:
                f['fields']['need_item_id'] = 0

            if not f['fields']['need_item_amount']:
                f['fields']['need_item_amount'] = 0

            f['fields']['attack_percent'] = float(f['fields']['attack_percent'])
            f['fields']['defense_percent'] = float(f['fields']['defense_percent'])
            f['fields']['manage_percent'] = float(f['fields']['manage_percent'])
            f['fields']['operation_percent'] = float(f['fields']['operation_percent'])

        return fixture


class StaffEquipmentQualityAddition(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.TextField(blank=True, verbose_name="说明")
    attack = models.IntegerField()
    attack_percent = models.DecimalField(max_digits=8, decimal_places=4)

    defense = models.IntegerField()
    defense_percent = models.DecimalField(max_digits=8, decimal_places=4)

    manage = models.IntegerField()
    manage_percent = models.DecimalField(max_digits=8, decimal_places=4)

    operation = models.IntegerField()
    operation_percent = models.DecimalField(max_digits=8, decimal_places=4)

    class Meta:
        db_table = 'staff_equipment_quality_addition'
        ordering = ('id',)
        verbose_name = "装备品质奖励"
        verbose_name_plural = "装备品质奖励"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['attack_percent'] = float(f['fields']['attack_percent'])
            f['fields']['defense_percent'] = float(f['fields']['defense_percent'])
            f['fields']['manage_percent'] = float(f['fields']['manage_percent'])
            f['fields']['operation_percent'] = float(f['fields']['operation_percent'])

        return fixture

class StaffEquipmentLevelAddition(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.TextField(blank=True, verbose_name="说明")
    attack = models.IntegerField()
    attack_percent = models.DecimalField(max_digits=8, decimal_places=4)

    defense = models.IntegerField()
    defense_percent = models.DecimalField(max_digits=8, decimal_places=4)

    manage = models.IntegerField()
    manage_percent = models.DecimalField(max_digits=8, decimal_places=4)

    operation = models.IntegerField()
    operation_percent = models.DecimalField(max_digits=8, decimal_places=4)

    class Meta:
        db_table = 'staff_equipment_level_addition'
        ordering = ('id',)
        verbose_name = "装备等级奖励"
        verbose_name_plural = "装备等级奖励"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['attack_percent'] = float(f['fields']['attack_percent'])
            f['fields']['defense_percent'] = float(f['fields']['defense_percent'])
            f['fields']['manage_percent'] = float(f['fields']['manage_percent'])
            f['fields']['operation_percent'] = float(f['fields']['operation_percent'])

        return fixture
