# -*- coding:utf-8 -*-

from django.db import models
# Create your models here.


TALENT_TYPE = (
        (1, "人族天赋"),
        (2, "神族天赋"),
        (3, "虫族天赋"),
    )


class Talent(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="天赋ID")
    # next_id 是用来升级的
    next_id = models.IntegerField(verbose_name="下一个级天赋ID")
    tp = models.IntegerField(choices=TALENT_TYPE, verbose_name="天赋类型")
    name = models.CharField(max_length=32, verbose_name="天赋名")
    effect_id = models.IntegerField(verbose_name="天赋效果")
    position = models.IntegerField(verbose_name="天赋位置")
    # unlock 三个值
    # 0： 表示新角色创建完就开启的
    # -1： 无法被其他talent开启，只能痛过升级升过来
    # N： N是其他talentID， 表示有N 这个talent ID 后，这个talent将被开启
    unlock = models.IntegerField(verbose_name="前置条件", db_index=True)
    up_need = models.IntegerField(verbose_name="消耗天赋点数")
    image = models.CharField(max_length=255, blank=True, verbose_name="天赋图片")
    des = models.TextField(verbose_name="天赋描述")


    class Meta:
        db_table = "talent"
        verbose_name = "天赋树"
        verbose_name_plural = "天赋树"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            trigger_unlock = Talent.objects.filter(unlock=f['pk']).values_list('id', flat=True)
            f['fields']['trigger_unlock'] = list(trigger_unlock)

        return fixture
