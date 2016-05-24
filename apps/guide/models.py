# -*- coding: utf-8 -*-

from django.db import models

POSITION = (
    (1, '左'),
    (2, '右'),
)

class Guide(models.Model):
    OPERATE_TYPE = (
        (0, '空操作'),
        (1, '点击UI'),
        (2, '拖动UI'),
        (3, '点击建筑')
    )

    ARROW = (
        (0, "没有箭头"),
        (1, "上"),
        (2, "下"),
        (3, "左"),
        (4, "右"),
    )

    id = models.IntegerField(primary_key=True)
    next_id = models.IntegerField(default=0, verbose_name='下一步ID')

    operate_type = models.IntegerField(choices=OPERATE_TYPE, verbose_name="操作类型")
    operate_target = models.CharField(max_length=255, blank=True, verbose_name="操作目标")

    resume_url = models.CharField(max_length=255, blank=True, verbose_name="恢复操作步骤")
    arrow = models.IntegerField(choices=ARROW, default=0, verbose_name="箭头方向")

    before_icon = models.CharField(max_length=255, blank=True)
    before_position = models.IntegerField(default=1, choices=POSITION)
    before_dialog = models.TextField(blank=True)

    after_icon = models.CharField(max_length=255, blank=True)
    after_position = models.IntegerField(default=1, choices=POSITION)
    after_dialog = models.TextField(blank=True)

    class Meta:
        db_table = 'guide'
        verbose_name = "新手引导"
        verbose_name_plural = "新手引导"

    @classmethod
    def patch_fixture(cls, fixture):
        def _make_dialog(d):
            return {
                'position': d.position,
                'icon': d.icon,
                'dialog': d.dialog
            }


        for f in fixture:
            before_icon = f['fields'].pop('before_icon')
            before_position = f['fields'].pop('before_position')
            before_dialog = f['fields'].pop('before_dialog')

            after_icon = f['fields'].pop('after_icon')
            after_position = f['fields'].pop('after_position')
            after_dialog = f['fields'].pop('after_dialog')

            if before_dialog:
                f['fields']['dialog_before'] = [{'position': before_position, 'icon': before_icon, 'dialog': before_dialog}]
            else:
                f['fields']['dialog_before'] = []

            if after_dialog:
                f['fields']['after_dialog'] = [{'position': after_position, 'icon': after_icon, 'dialog': after_dialog}]
            else:
                f['fields']['after_dialog'] = []

        return fixture


class GuideDialogBefore(models.Model):
    guide = models.ForeignKey(Guide, related_name='dialog_before')
    dialog = models.TextField()
    icon = models.CharField(max_length=255, verbose_name='小秘书图片')
    position = models.IntegerField(choices=POSITION, default=1, verbose_name='小秘书位置')

    class Meta:
        db_table = 'guide_dialog_before'
        verbose_name = "操作前对话"
        verbose_name_plural = "操作前对话"


class GuideDialogAfter(models.Model):
    guide = models.ForeignKey(Guide, related_name='dialog_after')
    dialog = models.TextField()
    icon = models.CharField(max_length=255, verbose_name='小秘书图片')
    position = models.IntegerField(choices=POSITION, default=1, verbose_name='小秘书位置')

    class Meta:
        db_table = 'guide_dialog_after'
        verbose_name = "操作后对话"
        verbose_name_plural = "操作后对话"
