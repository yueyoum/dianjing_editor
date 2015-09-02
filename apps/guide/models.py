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

    resume_url = models.CharField(max_length=255, blank=True, verbose_name="恢复操作步骤")

    class Meta:
        db_table = 'guide'
        verbose_name = "新手引导"
        verbose_name_plural = "新手引导"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            pk = f['pk']
            dialog_before = GuideDialogBefore.objects.filter(guide__id=pk).values_list('dialog', flat=True)
            dialog_after = GuideDialogAfter.objects.filter(guide__id=pk).values_list('dialog', flat=True)

            f['fields']['dialog_before'] = [x for x in dialog_before]
            f['fields']['dialog_after'] = [x for x in dialog_after]

        return fixture


class GuideDialogBefore(models.Model):
    guide = models.ForeignKey(Guide, related_name='dialog_before')
    dialog = models.TextField()

    class Meta:
        db_table = 'guide_dialog_before'
        verbose_name = "操作前对话"
        verbose_name_plural = "操作前对话"


class GuideDialogAfter(models.Model):
    guide = models.ForeignKey(Guide, related_name='dialog_after')
    dialog = models.TextField()

    class Meta:
        db_table = 'guide_dialog_after'
        verbose_name = "操作后对话"
        verbose_name_plural = "操作后对话"
