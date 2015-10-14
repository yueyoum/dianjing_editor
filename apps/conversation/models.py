# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.


class Conversation(models.Model):
    TRIGGER_TYPE = (
        (1, '点击建筑'),
        (2, '挑战关卡'),
        (3, '点击按钮')
    )

    TRIGGER_TIME = (
        (1, '战斗开始触发'),
        (2, '战斗结束触发'),
    )

    id = models.IntegerField(primary_key=True, verbose_name='会话id')
    tp = models.IntegerField(choices=TRIGGER_TYPE, verbose_name='触发条件')
    condition_value = models.CharField(max_length=64, verbose_name='条件值')
    is_loop = models.BooleanField(verbose_name='是否循环')
    time_tp = models.IntegerField(choices=TRIGGER_TIME, verbose_name='触发时间')
    conversation = models.TextField(verbose_name='剧情')

    class Meta:
        db_table = 'conversation'
        verbose_name = "剧情"
        verbose_name_plural = "剧情"

