# -*- coding: utf-8 -*-

from django.db import models

class SkillType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'skill_type'
        ordering = ('id',)
        verbose_name = '技能类型'
        verbose_name_plural = '技能类型'


class SkillAddition(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="名字")
    add_property = models.CharField(max_length=32, verbose_name="增加属性")
    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'skill_addition'
        ordering = ('id',)
        verbose_name = '技能加成'
        verbose_name_plural = '技能加成'


class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name='名字')
    icon = models.CharField(max_length=255, verbose_name="图标")
    type_id = models.ForeignKey(SkillType, db_column='type_id', verbose_name="类型")
    addition_ids = models.CharField(max_length=255, verbose_name="加成ID列表",
                                                     help_text='id:value,id:value'
                                                     )

    value_base = models.IntegerField("基础值")
    level_grow = models.IntegerField("等级增长", help_text="百分比数值")
    max_level = models.IntegerField("最大等级")

    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'skill'
        ordering = ('id',)
        verbose_name = '技能'
        verbose_name_plural = '技能'

