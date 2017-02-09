# -*- coding:utf-8 -*-

from django.db import models


class ChallengeConversation(models.Model):
    MODE = (
        (1, '战前'),
        (2, '战后'),
    )

    POS = (
        (1, '左边'),
        (2, '右边'),
    )


    id = models.IntegerField(primary_key=True)
    challenge_id = models.IntegerField()
    mode = models.IntegerField(choices=MODE)
    position = models.IntegerField(choices=POS)

    icon = models.CharField(max_length=255)
    dialog = models.TextField()

    class Meta:
        db_table = 'challenge_conversation'
        verbose_name = '挑战赛对话'
        verbose_name_plural = '挑战赛对话'
