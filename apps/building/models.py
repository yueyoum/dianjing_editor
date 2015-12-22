# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError


class Building(models.Model):
    LEVEL_UP_CONDITION_TYPE = (
        (1, "俱乐部等级"),
        (2, "俱乐部总部大楼等级"),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="名字")
    level_up_condition_type = models.IntegerField(choices=LEVEL_UP_CONDITION_TYPE, default=1, verbose_name="升级所需条件")
    des = models.TextField(blank=True, verbose_name="描述")
    status_des = models.TextField(blank=True, verbose_name="当前状态描述")
    remark = models.TextField(blank=True, verbose_name='备注')

    day_effect = models.CharField(max_length=255, blank=True, verbose_name='白天效果')
    night_effect = models.CharField(max_length=255, blank=True, verbose_name='晚上效果')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'building'
        verbose_name = '设施'
        verbose_name_plural = '设施'

    @classmethod
    def patch_fixture(cls, fixture):
        def get_need_items(items):
            need_items = []
            for item in items.split(','):
                item_id, item_amount = item.split(':')
                need_items.append((int(item_id), int(item_amount)))

            return need_items

        for f in fixture:
            bid = f['pk']
            f['fields'].pop('remark')
            levels = {}

            is_open = {}
            is_acc = {}
            for l in BuildingLevels.objects.filter(building__id=bid):
                levels[l.level] = {
                    'resource': l.resource,
                    'location': l.location,
                    'up_condition_value': l.up_condition_value,
                    'up_need_gold': l.up_need_gold,
                    'up_need_minutes': l.up_need_minutes,
                    'up_need_items': get_need_items(l.up_need_items),
                    'des': l.des,
                    'effect_des': l.effect_des,
                }

                effect = {}
                for e in BuildingEffectInfo.objects.filter(building_effect__id=l.effect.id):
                    if e.is_open:
                        is_open[e.tp] = e.value
                    elif e.is_acc:
                        is_acc[e.tp] = e.value
                    else:
                        effect[e.tp] = e.value
                if is_open:
                    effect += is_open
                if is_acc:
                    effect += is_acc

                levels[l.level]['effect'] = effect

            f['fields']['levels'] = levels

            if levels:
                max_levels = max(levels.keys())
            else:
                max_levels = 0

            f['fields']['max_levels'] = max_levels

        return fixture


class BuildingEffect(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="效果ID")
    name = models.CharField(max_length=255, verbose_name="建筑效果名")

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        db_table = "building_effect"
        verbose_name = "建筑效果"
        verbose_name_plural = "建筑效果"


class BuildingEffectInfo(models.Model):
    BUILDING_EFFECT_TYPE = (
        (1, "招募花费减少"),
        (2, "商务收益增加"),
        (3, "直播位置增加"),
        (4, "网店数量增加"),
        (5, "合约数量增加"),
        (6, "联赛经验增加"),
        (7, "天梯开放"),
        (8, "训练赛开放"),
        (9, "精英赛开放"),
        (10, "杯赛开放"),
        (11, "训练位置增加"),
        (12, "训练效果加成"),
        (13, "新的训练方式"),
    )

    building_effect = models.ForeignKey(BuildingEffect, related_name="effect_id")
    tp = models.IntegerField(choices=BUILDING_EFFECT_TYPE, verbose_name="效果类型")
    value = models.IntegerField(verbose_name="效果值")
    is_open = models.BooleanField(verbose_name="是否为开放类型")
    is_acc = models.BooleanField(verbose_name="是否为累加类型")

    class Meta:
        db_table = "building_effect_info"
        verbose_name = "建筑效果"
        verbose_name_plural = "建筑效果"


class BuildingLevels(models.Model):
    building = models.ForeignKey(Building, related_name='levels_info')
    level = models.IntegerField(verbose_name="等级", db_index=True)
    resource = models.CharField(max_length=255, blank=True, verbose_name="资源")
    location = models.CharField(max_length=255, blank=True, verbose_name="位置")
    up_condition_value = models.IntegerField(verbose_name="升级条件值")
    up_need_gold = models.IntegerField(default=0, verbose_name="升级所需软妹币")
    up_need_minutes = models.IntegerField(default=0, verbose_name='升级所需分钟数')
    up_need_items = models.CharField(max_length=255, verbose_name='所需物品', help_text='id:数量,id:数量')
    effect = models.ForeignKey(BuildingEffect, default=1, verbose_name="建筑效果")
    des = models.CharField(max_length=255, blank=True, verbose_name="描述")
    effect_des = models.CharField(max_length=255, blank=True, verbose_name="升级效果描述")

    def __unicode__(self):
        return u'#{0}'.format(self.level)

    class Meta:
        db_table = 'building_levels'

    def clean(self):
        from apps.item.models import Item
        for item in self.up_need_items.split(','):
            try:
                item_id, item_amount = item.split(':')
                item_id = int(item_id)
                item_amount = int(item_amount)
            except:
                raise ValidationError("所需物品填错了")

            if not Item.objects.filter(id=item_id).exists():
                raise ValidationError("物品{0}不存在".format(item_id))


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
    mail_title = models.CharField(max_length=255, verbose_name='邮件标题')
    mail_content = models.TextField(verbose_name='邮件内容')

    des = models.TextField(blank=True, verbose_name='描述')

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

    income = models.IntegerField(verbose_name='每天收入软妹币')
    income_des = models.TextField(blank=True, verbose_name='收入说明')
    condition_des = models.TextField(blank=True, verbose_name='条件说明')

    mail_title = models.CharField(max_length=255, verbose_name='邮件标题')
    mail_content = models.TextField(verbose_name='邮件内容')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'sponsor'
        verbose_name = '赞助商'
        verbose_name_plural = '赞助商'
