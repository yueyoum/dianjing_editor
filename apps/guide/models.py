# -*- coding: utf-8 -*-

from django.db import models

class Guide(models.Model):
    OPERATE_TYPE = (
        (1, '点击UI'),
        (2, '拖动UI'),
        (3, '点击建筑')
    )

    id = models.IntegerField(primary_key=True)
    next_id = models.IntegerField(default=0, verbose_name='下一步ID')

    operate_type = models.IntegerField(choices=OPERATE_TYPE, verbose_name="操作类型")
    operate_target = models.CharField(max_length=255, verbose_name="操作目标")

    resume_url = models.CharField(max_length=255, verbose_name="恢复操作步骤")

    class Meta:
        db_table = 'guide'
        verbose_name = "新手引导"
        verbose_name_plural = "新手引导"
