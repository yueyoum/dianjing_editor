# -*- coding: utf-8 -*-

from django.db import models

class Unit(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="兵种")
    race = models.ForeignKey('staff.StaffRace', verbose_name="种族")
    first_trig = models.IntegerField("开局触发值")
    second_trig = models.IntegerField("中间局触发值")
    third_trig = models.IntegerField("结束局触发值")
    skill = models.ForeignKey('skill.Skill', verbose_name="技能")

    des = models.TextField(blank=True, verbose_name="描述")


    def __unicode__(self):
        return self.name


    class Meta:
        db_table = 'unit'
        ordering = ('id',)
        verbose_name = "单位"
        verbose_name_plural = "单位"

