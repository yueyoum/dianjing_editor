from django.db import models
from apps.package import Package

# Create your models here.

class Task(models.Model):
    # 任务id
    id = models.IntegerField(primary_key=True, verbose_name="任务id")
    # 任务名称
    name = models.CharField(max_length=32, verbose_name="任务名")
    # 任务描述
    des = models.TextField(verbose_name="任务描述")
    # 任务类型
    type = models.ForeignKey('TaskType', verbose_name="任务类型")
    # 目标数量
    num = models.IntegerField(verbose_name="目标次数")
    # 任务奖励
    reward = models.ForeignKey('package.Package', verbose_name="任务奖励")

    class Meta:
        table_name = "task"
        ordering = "id"
        verbose_name = "任务"
        verbose_name_plural = "任务"

class TaskType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="类型id")
    name = models.CharField(max_length=32, verbose_name="类型名")

    class Meta:
        table_name = "task_type"
        verbose_name = "任务类型"
        verbose_name_plural = "任务类型"