# -*- coding: utf-8 -*-

from django.db import models

class TrainingType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32, verbose_name="名称")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'training_type'
        ordering = ('id',)
        verbose_name = "训练类型"
        verbose_name_plural = "训练类型"



class Training(models.Model):
    RewardType = (
        (1, "经验"),
        (2, "软妹币"),
        (3, "状态"),
        (10, "属性-随机"),
        (11, "属性-进攻"),
        (12, "属性-牵制"),
        (13, "属性-心态"),
        (14, "属性-暴兵"),
        (15, "属性-防守"),
        (16, "属性-运营"),
        (17, "属性-意识"),
        (18, "属性-操作"),
    )


    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32, verbose_name="名称")
    tp = models.ForeignKey(TrainingType, db_column='tp', verbose_name="类型")
    icon = models.CharField(max_length=32, verbose_name="图标")
    des = models.TextField(blank=True)

    minutes = models.IntegerField(verbose_name="训练所需分钟")
    reward_type = models.IntegerField(null=True, blank=True, choices=RewardType, verbose_name="奖励类型")
    reward_value = models.IntegerField(verbose_name="奖励值")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'training'
        ordering = ('id',)
        verbose_name = "训练"
        verbose_name_plural = "训练"
