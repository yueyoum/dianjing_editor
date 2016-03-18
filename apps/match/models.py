# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

from apps.staff.models import Staff
from apps.package.models import Package


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
        (9, "0<=, <10"),
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


class ChallengeChapter(models.Model):
    TP = (
        (1, '普通'),
        (2, '精英'),
    )

    id = models.IntegerField(primary_key=True)
    tp = models.IntegerField(choices=TP, verbose_name='类型')
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    des = models.TextField()
    star_reward = models.CharField(max_length=255, help_text='星数,奖励ID,奖励数量;...')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'challenge_chapter'
        verbose_name = '挑战赛章节'
        verbose_name_plural = '挑战赛章节'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            reward = f['fields']['star_reward']
            parsed_reward = []
            for x in reward.split(';'):
                a, b, c = x.split(',')
                parsed_reward.append((int(a), int(b), int(c)))

            f['fields']['star_reward'] = parsed_reward

        return fixture


class ChallengeMatch(models.Model):
    id = models.IntegerField(primary_key=True)
    area = models.CharField(max_length=255, verbose_name='大区名')
    chapter = models.IntegerField(verbose_name='章节')
    name = models.CharField(max_length=255, verbose_name="关卡名")
    des = models.TextField(verbose_name='描述')
    club_flag = models.CharField(max_length=255, verbose_name='旗帜')

    energy = models.IntegerField(verbose_name='消耗体力')
    club_exp = models.IntegerField(verbose_name='获得俱乐部经验')
    staffs = models.CharField(max_length=255, verbose_name='选手列表',
                              help_text='位置，ID，兵种ID；...'
                              )

    drop = models.CharField(max_length=255, verbose_name='掉落',
                            help_text='物品ID，数量，初始几率，递增几率；...'
                            )

    condition_challenge = models.IntegerField(verbose_name='前置关卡ID')
    times_limit = models.IntegerField(verbose_name='每日限制次数')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'challenge_match'
        verbose_name = '挑战赛'
        verbose_name_plural = '挑战赛'


    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            staffs = f['fields']['staffs']
            parsed_staffs = []
            for x in staffs.split(';'):
                a, b, c = x.split(',')
                parsed_staffs.append((int(a), int(b), int(c)))

            f['fields']['staffs'] = parsed_staffs

            drop = f['fields']['drop']
            parsed_drop = []
            for x in drop.split(';'):
                a, b, c, d = x.split(',')
                parsed_drop.append((int(a), int(b), int(c), int(d)))

            f['fields']['drop'] = parsed_drop

        return fixture


class Maps(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='名字')
    picture = models.CharField(max_length=255, verbose_name='图片')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'maps'
        verbose_name = '地图'
        verbose_name_plural = '地图'


class TrainingMatchReward(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="第几场")
    reward = models.ForeignKey('package.Package', verbose_name="奖励", related_name='tmr')
    score = models.IntegerField(verbose_name='获得积分')
    des = models.TextField(blank=True)

    class Meta:
        db_table = 'training_match_reward'
        verbose_name = '训练赛奖励'
        verbose_name_plural = '训练赛奖励'


class TrainingMatchScoreStore(models.Model):
    id = models.IntegerField(primary_key=True)
    times_limit = models.IntegerField(default=-1, verbose_name="次数限制",
                                      help_text="-1为没有限制，0为无法兑换，正整数N表示可以兑换N次")

    score = models.IntegerField(verbose_name="所需积分")

    item = models.ForeignKey('item.Item', verbose_name='物品')
    item_amount = models.IntegerField(default=1, verbose_name='物品数量')

    class Meta:
        db_table = 'training_match_score_store'
        verbose_name = "训练赛积分商店"
        verbose_name_plural = "训练赛积分商店"


class EliteArea(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='名字')
    need_club_level = models.IntegerField(verbose_name="所需俱乐部等级")
    match_ids = models.CommaSeparatedIntegerField(max_length=255, verbose_name='关卡ID列表')
    star_reward = models.CharField(max_length=255, verbose_name="星级奖励")
    map_name = models.CharField(max_length=255, verbose_name="地图")
    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'elite_area'
        verbose_name = '精英赛大区'
        verbose_name_plural = '精英赛大区'

    def clean(self):
        if not self.match_ids:
            return

        for i in self.match_ids.split(','):
            if not i.isdigit():
                raise ValidationError("关卡ID {0} 填错了".format(i))

            if not EliteMatch.objects.filter(id=int(i)).exists():
                raise ValidationError("关卡ID {0} 不存在".format(i))

        for v in self.star_reward.split(','):
            j, k = v.split(':')
            if not str(j).isdigit():
                raise ValidationError("星数必须是数字")

            if not str(k).isdigit():
                raise ValidationError("物品ID必须是数字")

            if not Package.objects.filter(id=int(k)).exists():
                raise ValidationError("物品ID {0} 不存在".format(k))

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            match_ids = f['fields']['match_ids']
            f['fields']['match_ids'] = [int(i) for i in match_ids.split(',')]

            star_reward = f['fields']['star_reward']
            reward = []
            for v in str(star_reward).split(','):
                i, j = v.split(':')
                reward.append({'star': int(i), 'reward': int(j)})

            f['fields']['star_reward'] = reward

        return fixture


class EliteMatch(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="名字")
    max_times = models.IntegerField(verbose_name="次数限制")

    club_name = models.CharField(max_length=255, verbose_name="关卡俱乐部名字")
    club_flag = models.ForeignKey('club.ClubFlag', verbose_name="关卡俱乐部旗帜")
    policy = models.ForeignKey('unit.Policy', verbose_name="战术")
    staff_level = models.IntegerField(verbose_name="选手等级")
    staffs = models.CommaSeparatedIntegerField(max_length=255, verbose_name="选手ID列表")

    reward = models.ForeignKey('package.Package', verbose_name="奖励物品包")

    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'elite_match'
        verbose_name = '精英赛小关卡'
        verbose_name_plural = '精英赛小关'

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
            f['fields']['staffs'] = [int(s) for s in staffs.split(',')]

        return fixture
