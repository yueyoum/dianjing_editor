# -*- coding: utf-8 -*-
from django.db import models
from apps.task.models import POSITION_TYPE


class ClientNPC(models.Model):
    FUNCTION = (
        (0, "没有功能"),
        (1, "任务"),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    model = models.CharField(max_length=255, verbose_name='模型')
    position = models.CharField(max_length=255, verbose_name='位置')

    function = models.IntegerField(default=0, choices=FUNCTION, verbose_name='功能')
    value = models.IntegerField(default=0, verbose_name='功能值')

    class Meta:
        db_table = 'client_npc'
        verbose_name = '客户端NPC'
        verbose_name_plural = '客户端NPC'

    @classmethod
    def patch_fixture(cls, fixture):
        def make_dialog(dialog):
            return {
                'position': dialog.position,
                'icon': dialog.icon,
                'dialog': dialog.dialog
            }

        for f in fixture:
            npc_dialog = ClientNPCDiaLog.objects.filter(npc_id=f['pk'])
            f['fields']['dialogs'] = [make_dialog(d) for d in npc_dialog]

        return fixture


class ClientNPCDiaLog(models.Model):
    npc = models.ForeignKey(ClientNPC)
    position = models.IntegerField(choices=POSITION_TYPE, verbose_name='对话者位置')
    icon = models.CharField(max_length=255, verbose_name='对话者图标')
    dialog = models.TextField(verbose_name='对话')

    class Meta:
        db_table = 'client_npc_dialog'
