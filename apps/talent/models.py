# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

from apps.skill.models import  TalentSkill

# Create your models here.


TALENT_TYPE = (
        (1, "人族天赋"),
        (2, "虫族天赋"),
        (3, "神族天赋"),
    )


class Talent(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="天赋ID")
    tp = models.IntegerField(choices=TALENT_TYPE, verbose_name="天赋类型")
    name = models.CharField(max_length=32, verbose_name="天赋名")
    effect_id = models.ForeignKey(TalentSkill, null=True, verbose_name="天赋效果")
    position = models.IntegerField(verbose_name="天赋位置")
    unlock = models.IntegerField(verbose_name="前置条件")
    up_need = models.CharField(max_length=32, verbose_name="消耗道具",
                               help_text='id,amounts;ld,amounts')
    image = models.CharField(max_length=255, verbose_name="天赋图片")
    des = models.TextField(verbose_name="天赋描述")

    class Meta:
        db_table = "talent"
        verbose_name = "天赋"
        verbose_name_plural = "天赋"

    def clean(self):
        if not TalentSkill.objects.filter(id=int(self.unlock)).exists():
            raise ValidationError("前置条件 {0} 不存在!".format(self.unlock))
