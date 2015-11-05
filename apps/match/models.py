# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

from apps.staff.models import Staff


class MatchConversationStart(models.Model):
    id = models.IntegerField(primary_key=True)
    policy = models.ForeignKey('unit.Policy', verbose_name="战术")
    race = models.ForeignKey('staff.StaffRace', verbose_name="种族")
    des = models.TextField(verbose_name="描述")

    class Meta:
        db_table = 'match_conversation_start'
        verbose_name = '每局比赛开始对话'
        verbose_name_plural = '每局比赛开始对话'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['des'] = f['fields']['des'].split('|')

        return fixture


class MatchConversationEnd(models.Model):
    END_AT = (
        (1, "第一回合"),
        (2, "第二回合"),
        (3, "第三回合"),
    )

    VALUE = (
        (50, "=50"),
        (49, "40<=, <50"),
        (39, "30<=, <40"),
        (29, "20<=, <30"),
        (19, "10<=, <20"),
        (9,  "0<=, <10"),
        (0, "无关紧要"),
    )

    id = models.IntegerField(primary_key=True)
    end_at = models.IntegerField(choices=END_AT, verbose_name="结束于")
    disadvantage_win = models.BooleanField(default=False, verbose_name="劣势方是否胜利")
    disadvantage_value = models.IntegerField(choices=VALUE, null=True, blank=True, verbose_name="劣势方优势值")

    des = models.TextField(verbose_name="描述")

    class Meta:
        db_table = 'match_conversation_end'
        verbose_name = '每局比赛结束对话'
        verbose_name_plural = '每局比赛结束对话'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['des'] = f['fields']['des'].split('|')

        return fixture

class MatchConversationRoundEnd(models.Model):
    ROUND = (
        (1, "第一回合"),
        (2, "第二回合"),
        (3, "第三回合"),
    )

    id = models.IntegerField(primary_key=True, choices=ROUND, verbose_name="第几回合")
    des = models.TextField(verbose_name="描述")

    class Meta:
        db_table = 'match_conversation_round_end'
        verbose_name = '每回合比赛结束对话'
        verbose_name_plural = '每回合比赛结束对话'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['des'] = f['fields']['des'].split('|')

        return fixture

class ChallengeType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='类型')
    level = models.IntegerField(verbose_name="等级")
    color = models.CharField(max_length=255, verbose_name='颜色')
    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'challenge_type'
        verbose_name = '挑战赛类型'
        verbose_name_plural = '挑战赛类型'


class ChallengeMatch(models.Model):
    id = models.IntegerField(primary_key=True)
    next_id = models.IntegerField(verbose_name="下一关ID")
    name = models.CharField(max_length=255, verbose_name="名字")
    club_name = models.CharField(max_length=255, verbose_name="俱乐部名字")
    club_flag = models.ForeignKey('club.ClubFlag', verbose_name="俱乐部旗帜")
    tp = models.ForeignKey(ChallengeType, verbose_name="类型")
    policy = models.ForeignKey('unit.Policy', verbose_name="战术")

    level = models.IntegerField(verbose_name="选手等级")
    strength = models.FloatField(verbose_name="选手强度系数")

    staffs = models.CommaSeparatedIntegerField(max_length=255, verbose_name="选手ID列表")
    winning_rates = models.CommaSeparatedIntegerField(max_length=255, default='1,1,1,1,1', verbose_name="胜率列表")

    package = models.ForeignKey('package.Package', verbose_name="奖励物品包")

    des = models.TextField(blank=True, verbose_name="描述")


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'challenge_match'
        verbose_name = '挑战赛'
        verbose_name_plural = '挑战赛'


    def clean(self):
        staffs = [int(s) for s in self.staffs.split(',')]
        if len(staffs) != 5:
            raise ValidationError("wrong staffs")

        for s in staffs:
            if not Staff.objects.filter(id=int(s)).exists():
                raise ValidationError("Staff {0} not exists".format(s))

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            staffs = f['fields']['staffs']
            winning_rates = f['fields']['winning_rates']
            f['fields']['staffs'] = [int(s) for s in staffs.split(',')]
            f['fields']['winning_rates'] = [int(s) for s in winning_rates.split(',')]

        return fixture


class Maps(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='名字')
    picture = models.CharField(max_length=255, verbose_name='图片')

    class Meta:
        db_table = 'maps'
        verbose_name = '地图'
        verbose_name_plural = '地图'
