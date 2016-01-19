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
    )

    id = models.IntegerField(primary_key=True)
    effect = models.CharField(max_length=255)
    race = models.IntegerField(choices=RACE, verbose_name="种族")
    tp = models.IntegerField(choices=TYPE, verbose_name="类型")

    class Meta:
        db_table = 'unit_effect'
        verbose_name = "单位特效"
        verbose_name_plural = "单位特效"
