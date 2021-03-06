# -*- coding: utf-8 -*-

from django.db import models


class Function(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    belong_to_building = models.IntegerField(verbose_name="所属建筑")
    belong_to_ui = models.CharField(max_length=255, blank=True)
    order_in_building = models.IntegerField(default=1, verbose_name="在界面中显示顺序")
    need_club_level = models.IntegerField(default=1, verbose_name="所需俱乐部等级")
    need_challenge_id = models.IntegerField(default=0, verbose_name='所需关卡ID')
    unlock_des = models.TextField(blank=True, verbose_name="解锁描述")

    normal_color = models.CharField(max_length=255, blank=True)
    lock_color = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'function'
        verbose_name = "功能"
        verbose_name_plural = "功能"


class FunctionTips(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.IntegerField()
    tp = models.IntegerField()
    target = models.CharField(max_length=255)
    des = models.TextField()

    class Meta:
        db_table = 'function_tips'
        verbose_name = "功能开放提示"
        verbose_name_plural = "功能开放提示"