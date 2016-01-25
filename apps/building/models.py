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
                for info in BuildingEffectInfo.objects.filter(building_effect__id=l.effect.id):
                    if info.tp == 7:
                        is_open[info.tp] = info.value
                    else:
                        effect[info.tp] = info.value

                effect = effect.items() + is_open.items()
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
        (3, "直播位置累计增加"),
        (4, "网店数量累计增加"),
        (5, "合约数量累计增加"),
        (6, "联赛经验增加"),
        (7, "功能开放"),
        (8, "训练位置累计增加"),
        (9, "训练效果加成"),
    )

    building_effect = models.ForeignKey(BuildingEffect, related_name="effect_id")
    tp = models.IntegerField(choices=BUILDING_EFFECT_TYPE, verbose_name="效果类型")
    value = models.CharField(max_length=255, verbose_name="效果值")

    class Meta:
        db_table = "building_effect_info"
        verbose_name = "建筑效果"
        verbose_name_plural = "建筑效果"

        unique_together = (
            ('building_effect', 'tp'),
        )

    def clean(self):
        from apps.function.models import Function
        if self.tp == 7:
            function_list = []
            for function in self.value.split(','):
                try:
                    function = int(function)
                except:
                    raise ValidationError("开放功能id填错了")

                if not Function.objects.filter(id=function).exists():
                    raise ValidationError("功能{0}不存在".format(function))

                if function in function_list:
                    raise ValidationError("功能{0}不能反复添加".format(function))
                else:
                    function_list.append(function)
        else:
            try:
                value = int(self.value)
            except:
                raise ValidationError("数值填错了")


class BuildingLevels(models.Model):
    building = models.ForeignKey(Building, related_name='levels_info')
    level = models.IntegerField(verbose_name="等级", db_index=True)
    resource = models.CharField(max_length=255, blank=True, verbose_name="资源")
    location = models.CharField(max_length=255, blank=True, verbose_name="位置")
    up_condition_value = models.IntegerField(verbose_name="升级条件值")
    up_need_gold = models.IntegerField(default=0, verbose_name="升级所需软妹币")
    up_need_minutes = models.IntegerField(default=0, verbose_name='升级所需分钟数')
    up_need_items = models.CharField(max_length=255, verbose_name='所需物品', help_text='id:数量,id:数量')
    effect = models.ForeignKey(BuildingEffect, null=True, blank=True, verbose_name="建筑效果")
    des = models.CharField(max_length=255, blank=True, verbose_name="描述")
    effect_des = models.CharField(max_length=255, blank=True, verbose_name="升级效果描述")

    def __unicode__(self):
        return u'#{0}'.format(self.level)

    class Meta:
        db_table = 'building_levels'

    def clean(self):
        if not self.effect:
            raise ValidationError("-->建筑效果<-- 不能为空!")

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

    goods = models.ForeignKey('item.Item', null=True, blank=True, verbose_name="售卖货物")
    goods_max_amount = models.IntegerField(verbose_name="货物最大数量", default=1000)
    sells_per_hour = models.IntegerField(verbose_name="每小时卖多少个", default=0)

    mail_title = models.CharField(max_length=255, verbose_name='邮件标题')
    mail_content = models.TextField(verbose_name='邮件内容')

    des = models.TextField(blank=True, verbose_name='描述')

    def __unicode__(self):
        return self.name

    def clean(self):
        if not self.goods:
            raise ValidationError("货物不能为空")

    class Meta:
        db_table = 'business_shop'
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
        db_table = 'business_sponsor'
        verbose_name = '赞助商'
        verbose_name_plural = '赞助商'


class BusinessBroadcastReward(models.Model):
    id = models.OneToOneField('item.Item', verbose_name="物品", primary_key=True)
    amount = models.IntegerField(verbose_name="数量")
    prob = models.IntegerField(default=100, verbose_name="概率")

    class Meta:
        db_table = 'business_broadcast_reward'
        verbose_name = '直播获得物品'
        verbose_name_plural = '直播获得物品'
