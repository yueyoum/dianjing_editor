# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class TaskType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="类型id")
    name = models.CharField(unique=True, max_length=32, verbose_name="类型名")
    des = models.TextField(default=None, verbose_name="类型描述")

    # unicode显示名称
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "task_type"
        verbose_name = "任务类型"
        verbose_name_plural = "任务类型"

class Task(models.Model):
    # 任务id
    id = models.IntegerField(primary_key=True, verbose_name="任务id")
    # 任务名称
    name = models.CharField(max_length=32, verbose_name="任务名")
    # 任务中心等级
    level = models.IntegerField(verbose_name="所需任务中心等级")
    # 任务描述
    des = models.TextField(verbose_name="任务描述")
    # 任务类型
    tp = models.ForeignKey(TaskType, verbose_name="任务类型")
    # 目标数量
    num = models.IntegerField(verbose_name="目标次数")
    # 任务奖励
    reward = models.ForeignKey('package.Package', verbose_name="任务奖励")

    class Meta:
        db_table = "task"
        ordering = ('id',)
        verbose_name = "任务"
        verbose_name_plural = "任务"
