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
    id = models.IntegerField(primary_key=True)
    icon = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=32, verbose_name="兵种")
    race = models.ForeignKey('staff.StaffRace', verbose_name="种族")
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
