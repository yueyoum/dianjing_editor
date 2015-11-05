# -*- coding: utf-8 -*-

from django.db import models

class ClubFlag(models.Model):
    id = models.IntegerField(primary_key=True)
    flag = models.CharField(max_length=255, verbose_name="旗帜")

    def __unicode__(self):
        return self.flag

    class Meta:
        db_table = 'club_flag'
        verbose_name = "俱乐部旗帜"
        verbose_name_plural = "俱乐部旗帜"


class ClubLevel(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="等级")
    renown = models.IntegerField(verbose_name="升到下一级所需声望")
    max_staff_amount = models.IntegerField(verbose_name="最大员工数")

    def __unicode__(self):
        return u'%d' % self.id

    class Meta:
        db_table = 'club_level'
        verbose_name = "俱乐部等级"
        verbose_name_plural = "俱乐部等级"

class TibuSlot(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="数量")
    need_club_level = models.IntegerField(verbose_name='所需俱乐部等级')
    des = models.TextField(verbose_name='描述')

    class Meta:
        db_table = 'tibu_slot'
        verbose_name = '替补格子'
        verbose_name_plural = '替补格子'
