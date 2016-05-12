# -*- coding:utf-8 -*-

from django.db import models

# from apps.building.models import Building
# from apps.match.models import ChallengeMatch


# Create your models here.


class Conversation(models.Model):
    TRIGGER_TYPE = (
        (1, '点击建筑'),
        (2, '挑战关卡'),
        (3, '点击按钮')
    )

    TRIGGER_TIME = (
        (1, '战斗开始触发'),
        (2, '战斗结束触发'),
    )

    id = models.IntegerField(primary_key=True, verbose_name='会话id')
    tp = models.IntegerField(choices=TRIGGER_TYPE, verbose_name='触发条件')
    condition_value = models.CharField(max_length=255, verbose_name='条件值')
    is_loop = models.BooleanField(verbose_name='是否循环')
    time_tp = models.IntegerField(choices=TRIGGER_TIME, verbose_name='触发时间')

    # def clean(self):
    #     if self.tp == 1:
    #         if not self.condition_value.isdigit() or \
    #                 not Building.objects.filter(id=int(self.condition_value)).exists():
    #             raise ValidationError("Building {0} not exists".format(self.condition_value))
    #
    #     if self.tp == 2:
    #         if not self.condition_value.isdigit() or \
    #                 not ChallengeMatch.objects.filter(id=int(self.condition_value)).exists():
    #             raise ValidationError("ChallengeMatch {0} not exists".format(self.condition_value))

    class Meta:
        db_table = 'conversation'
        verbose_name = "剧情"
        verbose_name_plural = "剧情"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            conversations = []
            for _r in ConversationInfo.objects.filter(conversation__id=f['pk']):
                conversation_info = {}
                conversation_info['position'] = _r.position
                conversation_info['icon'] = _r.icon
                conversation_info['dialog'] = _r.dialog
                conversations.append(conversation_info)

            f['fields']['conversations'] = conversations

        return fixture


class ConversationInfo(models.Model):
    POSITION_TYPE = (
        (1, '在左边'),
        (2, '在右边')
    )

    conversation = models.ForeignKey(Conversation)
    position = models.IntegerField(choices=POSITION_TYPE, verbose_name='会话者位置')
    icon = models.CharField(max_length=255, verbose_name='会话者图标')
    dialog = models.TextField(verbose_name='会话内容')

    class Meta:
        db_table = 'conversation_info'
