# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError


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


class StaffQuality(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    color = models.CharField(max_length=32)
    icon = models.CharField(max_length=255, blank=True)
    background = models.CharField(max_length=255, blank=True)
    background_half = models.CharField(max_length=255, blank=True, verbose_name="半身像")

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = "staff_quality"
        verbose_name = "品质"
        verbose_name_plural = "品质"


class StaffStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    icon = models.CharField(max_length=255, blank=True, verbose_name="图标")
    name = models.CharField(max_length=32, verbose_name="名称")
    value = models.IntegerField(verbose_name="加成值", help_text="5% 直接填5")
    des = models.CharField(max_length=255, verbose_name="说明", blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'staff_status'
        verbose_name = "状态"
        verbose_name_plural = "状态"


class StaffLevel(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="等级")
    quality_A = models.IntegerField(verbose_name="品质A升级所需经验")
    quality_B = models.IntegerField(verbose_name="品质B升级所需经验")
    quality_C = models.IntegerField(verbose_name="品质C升级所需经验")
    quality_S = models.IntegerField(verbose_name="品质S升级所需经验")
    quality_SS = models.IntegerField(verbose_name="品质SS升级所需经验")

    def __unicode__(self):
        return u'%d' % self.id

    class Meta:
        db_table = 'staff_level'
        verbose_name = "等级"
        verbose_name_plural = "等级"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            exp = {}
            for k, v in f['fields'].iteritems():
                _, quality = k.split('_')
                exp[quality] = v

            f['fields'] = {'exp': exp}

        return fixture


class Staff(models.Model):
    BUY_TYPE = (
        (1, "RMB"),
        (2, "钻石")
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32, verbose_name="名字")
    avatar = models.CharField(max_length=32, verbose_name="头像")
    picture = models.CharField(max_length=255, verbose_name="半身像")
    nation = models.CharField(max_length=32, verbose_name="国籍")
    gender = models.CharField(max_length=32, verbose_name="性别")

    race = models.ForeignKey(StaffRace, db_column='race', verbose_name="种族")
    quality = models.ForeignKey(StaffQuality, db_column='quality', verbose_name="品质")

    buy_type = models.IntegerField(choices=BUY_TYPE, verbose_name="签约费类型")
    buy_cost = models.IntegerField(verbose_name="签约费")
    can_recruit = models.BooleanField(verbose_name="是否可以招募", default=True)

    salary = models.IntegerField(verbose_name="薪水", default=0)

    skill_ids = models.CommaSeparatedIntegerField(max_length=255, blank=True, verbose_name="技能ID列表")
    qianban_ids = models.CommaSeparatedIntegerField(max_length=255, blank=True, verbose_name="牵绊ID列表")

    des = models.TextField(blank=True, verbose_name="简介")

    luoji = models.IntegerField(default=0, verbose_name="逻辑")
    minjie = models.IntegerField(default=0, verbose_name="敏捷")
    lilun = models.IntegerField(default=0, verbose_name="理论")
    wuxing = models.IntegerField(default=0, verbose_name="悟性")
    meili = models.IntegerField(default=0, verbose_name="魅力")

    def clean(self):
        from apps.skill.models import Skill
        from apps.qianban.models import QianBan

        if self.skill_ids:
            for i in self.skill_ids.split(','):
                if not Skill.objects.filter(id=int(i)).exists():
                    raise ValidationError("skill {0} not exists".format(i))

        if self.qianban_ids:
            for i in self.qianban_ids.split(','):
                if not QianBan.objects.filter(id=int(i)).exists():
                    raise ValidationError("qianban {0} not exists".format(i))

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'staff'
        verbose_name = "员工"
        verbose_name_plural = "员工"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            skill_ids = f['fields']['skill_ids']
            if skill_ids:
                f['fields']['skill_ids'] = [int(i) for i in skill_ids.split(',')]
            else:
                f['fields']['skill_ids'] = []

            qianban_ids = f['fields']['qianban_ids']
            if qianban_ids:
                f['fields']['qianban_ids'] = [int(i) for i in qianban_ids.split(',')]
            else:
                f['fields']['qianban_ids'] = []

        return fixture


class StaffHot(models.Model):
    id = models.OneToOneField(Staff, primary_key=True, verbose_name="员工")
    cost = models.IntegerField(verbose_name="花费")

    class Meta:
        db_table = "staff_hot"
        verbose_name = "员工招募-人气王"
        verbose_name_plural = "员工招募-人气王"


class StaffRecruitSettings(models.Model):
    recruit = models.ForeignKey('StaffRecruit', related_name='statff_settings')
    quality = models.ForeignKey(StaffQuality, verbose_name="品质")
    first_amount = models.IntegerField(verbose_name="首次刷新出现次数")
    lucky_amount = models.IntegerField(verbose_name="幸运刷新出现次数")
    normal_amount = models.IntegerField(verbose_name="平时出现次数")

    class Meta:
        db_table = 'staff_recruit_settings'
        unique_together = (('recruit', 'quality'),)


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


class StaffLevelNew(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='等级')
    exp = models.IntegerField(verbose_name='所需经验', null=True, blank=True)

    class Meta:
        db_table = 'staff_level_new'
        verbose_name = "选手等级（新）"
        verbose_name_plural = "选手等级（新）"


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

    update_item_need = models.CharField(max_length=255, blank=True, verbose_name='升到本阶所需道具',
                                        help_text='id,数量;id,数量...')

    level_limit = models.IntegerField(verbose_name='选手等级限制', null=True, blank=True)

    class Meta:
        db_table = 'staff_step'
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
        verbose_name = "选手升星（新）"
        verbose_name_plural = "选手升星（新）"