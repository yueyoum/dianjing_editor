# -*- coding: utf-8 -*-

from django.db import models

class ChallengeArea(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    class Meta:
        db_table = 'challenge_area'
        verbose_name = '挑战赛大区'
        verbose_name_plural = '挑战赛大区'

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
    area = models.IntegerField()
    map_name = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'challenge_chapter'
        verbose_name = '挑战赛章节'
        verbose_name_plural = '挑战赛章节'

    @classmethod
    def get_fixture_key(cls):
        return 'match.ChallengeChapter'

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

    condition_challenge = models.IntegerField(db_index=True, verbose_name='前置关卡ID')
    times_limit = models.IntegerField(verbose_name='每日限制次数')
    show_item_id = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'challenge_match'
        verbose_name = '挑战赛'
        verbose_name_plural = '挑战赛'

    @classmethod
    def get_fixture_key(cls):
        return 'match.ChallengeMatch'

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

            next_challenges = ChallengeMatch.objects.filter(condition_challenge=f['pk']).values_list('id', flat=True)
            f['fields']['next'] = list(next_challenges)

        return fixture


class ChallengeGuide(models.Model):
    id = models.IntegerField(primary_key=True)
    guide = models.IntegerField()
    des = models.TextField()
    return_to_main_panel = models.BooleanField()

    class Meta:
        db_table = 'challenge_guide'
        verbose_name = '挑战赛引导'
        verbose_name_plural = '挑战赛引导'


class ChallengeBuyCost(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='购买次数')
    diamond = models.IntegerField(verbose_name='钻石')

    class Meta:
        db_table = 'challenge_buy_cost'
        verbose_name = "挑战赛购买花费"
        verbose_name_plural = "挑战赛购买花费"
