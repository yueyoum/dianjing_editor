# -*- coding: utf-8 -*-

from django.db import models


class Building(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="名字")
    des = models.TextField(blank=True, verbose_name="描述")
    status_des = models.TextField(blank=True, verbose_name="当前状态描述")
    remark = models.TextField(blank=True, verbose_name='备注')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'building'
        verbose_name = '设施'
        verbose_name_plural = '设施'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            bid = f['pk']
            f['fields'].pop('remark')
            levels = {}
            for l in BuildingLevels.objects.filter(building__id=bid):
                levels[l.level] = {
                    'resource': l.resource,
                    'location': l.location,
                    'up_need_club_level': l.up_need_club_level,
                    'up_need_gold': l.up_need_gold,
                    'up_need_minutes': l.up_need_minutes,
                    'value1': l.value1 if l.value1 else 0,
                    'value2': l.value2 if l.value2 else 0,
                    'des': l.des,
                }

            f['fields']['levels'] = levels

            if levels:
                max_levels = max(levels.keys())
            else:
                max_levels = 0

            f['fields']['max_levels'] = max_levels

        return fixture


class BuildingLevels(models.Model):
    building = models.ForeignKey(Building, related_name='levels_info')
    level = models.IntegerField(verbose_name="等级", db_index=True)
    resource = models.CharField(max_length=255, blank=True, verbose_name="资源")
    location = models.CharField(max_length=255, blank=True, verbose_name="位置")
    up_need_club_level = models.IntegerField(verbose_name="升级所需俱乐部等级")
    up_need_gold = models.IntegerField(default=0, verbose_name="升级所需软妹币")
    up_need_minutes = models.IntegerField(default=0, verbose_name='升级所需分钟数')
    value1 = models.IntegerField(null=True, blank=True, verbose_name="值1")
    value2 = models.IntegerField(null=True, blank=True, verbose_name="值2")
    des = models.CharField(max_length=255, blank=True, verbose_name="描述")

    def __unicode__(self):
        return u'#{0}'.format(self.level)

    class Meta:
        db_table = 'building_levels'



class Shop(models.Model):
    UNLOCK_TYPE = (
        (1, '无需解锁'),
        (2, '俱乐部等级'),
        (3, 'VIP等级'),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='名字')

    unlock_type = models.IntegerField(choices=UNLOCK_TYPE, verbose_name='解锁条件')
    unlock_value = models.IntegerField(default=0, verbose_name='解锁值')

    income = models.IntegerField(verbose_name='每天获得软妹币')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'shop'
        verbose_name = '网店'
        verbose_name_plural = '网店'


class Sponsor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='名字')
    icon = models.CharField(max_length=255, verbose_name='图标')
    condition = models.ForeignKey('match.ChallengeMatch', verbose_name='需要通过的挑战赛')
    total_days = models.IntegerField(default=0, verbose_name='合约天数')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'sponsor'
        verbose_name = '赞助商'
        verbose_name_plural = '赞助商'
