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
    next_id = models.IntegerField(verbose_name="下一个级天赋ID")
    tp = models.IntegerField(choices=TALENT_TYPE, verbose_name="天赋类型")
    name = models.CharField(max_length=32, verbose_name="天赋名")
    effect_id = models.IntegerField(verbose_name="天赋效果")
    position = models.IntegerField(verbose_name="天赋位置")
    unlock = models.IntegerField(verbose_name="前置条件")
    up_need = models.CharField(max_length=255, blank=True, verbose_name="消耗物品",
                               help_text="ID,Number;ID,Number...")
    image = models.CharField(max_length=255, blank=True, verbose_name="天赋图片")
    des = models.TextField(verbose_name="天赋描述")

    class Meta:
        db_table = "talent"
        verbose_name = "天赋树"
        verbose_name_plural = "天赋树"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            need_item = []
            if f['fields']['up_need']:
                for pair in f['fields']['up_need'].split(";"):
                    item_id, amounts = pair.split(',')
                    need_item.append((int(item_id), int(amounts)))
            f['fields']['up_need'] = need_item

            if f['fields']['unlock']:
                for d in fixture:
                    if d['pk'] == f['fields']['unlock']:
                        trigger_unlock = []
                        if d['fields'].get('trigger_unlock', {}):
                            trigger_unlock = d['fields']['trigger_unlock']

                        trigger_unlock.append(f['pk'])
                        d['fields']['trigger_unlock'] = trigger_unlock

        return fixture


