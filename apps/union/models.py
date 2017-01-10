# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from misc import parse_text, parse_text_split_by_comma

class UnionLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    contribution = models.IntegerField()
    members_limit = models.IntegerField()

    class Meta:
        db_table = 'union_level'
        verbose_name = '公会等级'
        verbose_name_plural = '公会等级'


class UnionSignIn(models.Model):
    id = models.IntegerField(primary_key=True)
    contribution = models.IntegerField()
    rewards = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    vip = models.IntegerField()

    class Meta:
        db_table = 'union_singin'
        verbose_name = '公会签到'
        verbose_name_plural = '公会签到'

    @classmethod
    def patch_fixture(cls, fixture):
        def _parse(text):
            result = []
            for x in text.split(';'):
                if not x:
                    continue

                a, b = x.split(',')
                result.append((int(a), int(b)))

            return result

        for f in fixture:
            f['fields']['rewards'] = _parse(f['fields']['rewards'])
            f['fields']['cost'] = _parse(f['fields']['cost'])

        return fixture

class UnionExplore(models.Model):
    id = models.IntegerField(primary_key=True)
    staffs = models.CharField(max_length=255)
    explore_reward = models.TextField()
    harass_reward = models.TextField()

    class Meta:
        db_table = 'union_explore'
        verbose_name = '公会探索/骚扰'
        verbose_name_plural = '公会探索/骚扰'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['staffs'] = parse_text_split_by_comma(f['fields']['staffs'])
            f['fields']['explore_reward'] = parse_text(f['fields']['explore_reward'], 2)
            f['fields']['harass_reward'] = parse_text(f['fields']['harass_reward'], 2)

        return fixture

class UnionExploreRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    rank_des = models.CharField(max_length=255)
    reward = models.TextField()
    mail_title = models.CharField(max_length=255)
    mail_content = models.TextField()

    class Meta:
        db_table = 'union_explore_rank_reward'
        verbose_name = '公会探索度排名奖励'
        verbose_name_plural = '公会探索度排名奖励'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['reward'] = parse_text(f['fields']['reward'], 2)

        return fixture

class UnionMemberExploreRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    rank_des = models.CharField(max_length=255)
    reward = models.TextField()
    mail_title = models.CharField(max_length=255)
    mail_content = models.TextField()

    class Meta:
        db_table = 'union_member_explore_rank_reward'
        verbose_name = '个人探索度排名奖励'
        verbose_name_plural = '个人探索度排名奖励'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['reward'] = parse_text(f['fields']['reward'], 2)

        return fixture

class UnionHarassBuyTimesCost(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='购买次数')
    diamond = models.IntegerField()

    class Meta:
        db_table = 'union_harass_buy_times_cost'
        verbose_name = '骚扰购买次数消费'
        verbose_name_plural = "骚扰购买次数消费"


class UnionSkill(models.Model):
    id = models.IntegerField(primary_key=True)
    skill_id = models.IntegerField()
    level = models.IntegerField()
    name = models.CharField(max_length=255)
    des = models.TextField(blank=True)

    level_up_cost = models.TextField(blank=True)
    talent_id = models.IntegerField()

    class Meta:
        db_table = 'union_skill'
        verbose_name = '公会技能'
        verbose_name_plural = '公会技能'

    @classmethod
    def patch_fixture(cls, fixture):
        skills = {}
        for f in fixture:
            meta_data = f['fields']
            sid = meta_data.pop('skill_id')
            lv = meta_data.pop('level')

            if not meta_data['level_up_cost']:
                meta_data['level_up_cost'] = []
            else:
                meta_data['level_up_cost'] = parse_text(meta_data['level_up_cost'], 2)

            if sid not in skills:
                skills[sid] = {'levels': {lv: meta_data}}
            else:
                skills[sid]['levels'][lv] = meta_data

        new_fixture = []
        for sid, data in skills.iteritems():
            data['max_level'] = max(data['levels'].keys())

            this_fixture = {
                'pk': sid,
                'fields': data
            }

            new_fixture.append(this_fixture)

        return new_fixture
