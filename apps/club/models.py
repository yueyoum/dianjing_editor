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

    def __unicode__(self):
        return u'%d' % self.id

    class Meta:
        db_table = 'club_level'
        verbose_name = "俱乐部等级"
        verbose_name_plural = "俱乐部等级"

