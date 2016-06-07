# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

GoodsType = (
    (1, '普通商品'),
    (2, '高级商品'),
)


class TowerSaleGoods(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="商品ID")
    tp = models.IntegerField(choices=GoodsType, verbose_name="物品类别")
    tp_icon = models.CharField(max_length=255, verbose_name="类别icon")
    price_original = models.IntegerField(verbose_name="商品价格")
    price_now = models.IntegerField(verbose_name="促销价")
    vip_need = models.IntegerField(default=0, verbose_name="所需vip等级")

    item_id = models.IntegerField(verbose_name="物品ID")
    amount = models.IntegerField(verbose_name="数量")
    des = models.CharField(max_length=255, blank=True, verbose_name="描述")

    class Meta:
        db_table = 'tower_sale_goods'
        verbose_name = '促销商品'
        verbose_name_plural = '促销商品'


class TowerStarReward(models.Model):
    id = models.IntegerField(primary_key=True)
    reward = models.CharField(max_length=255, verbose_name="星级奖励", help_text="物品ID,数量;物品ID,数量")

    class Meta:
        db_table = 'tower_star_reward'
        verbose_name = '星级奖励'
        verbose_name_plural = '星级奖励'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            rewards = []
            for reward in f['fields']['reward'].split(';'):
                if not reward:
                    continue

                _id, _amount = reward.split(',')
                rewards.append([int(_id), int(_amount)])
            f['fields']['reward'] = rewards

        return fixture


class TowerRankReward(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="排名上限")
    rank_des = models.CharField(max_length=255, blank=True)
    reward = models.CharField(max_length=255, verbose_name="排名奖励", help_text="物品ID,数量;物品ID,数量")
    mail_title = models.CharField(max_length=255)
    mail_content = models.CharField(max_length=255)

    class Meta:
        db_table = 'tower_rank_reward'
        verbose_name = '排名奖励'
        verbose_name_plural = '排名奖励'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            rewards = []
            for reward in f['fields']['reward'].split(';'):
                if not reward:
                    continue

                _id, _amount = reward.split(',')
                rewards.append([int(_id), int(_amount)])
            f['fields']['reward'] = rewards

        return fixture


class TowerGameLevel(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="层级ID")
    name = models.CharField(max_length=32, verbose_name="层级名")
    talent_id = models.IntegerField(verbose_name="副本效果")
    staffs = models.CharField(max_length=255, verbose_name="npc配置",
                                help_text="位置,选手ID,兵种ID;位置,选手ID,兵种ID(位置范围0~29)")
    star_reward_1 = models.CharField(max_length=255, blank=True, verbose_name="1星奖励",
                                help_text="物品ID,数量;物品ID,数量...")
    star_reward_2 = models.CharField(max_length=255, blank=True, verbose_name="2星奖励",
                                help_text="物品ID,数量;物品ID,数量...")
    star_reward_3 = models.CharField(max_length=255, blank=True, verbose_name="3星奖励",
                                  help_text="物品ID,数量;物品ID,数量...")

    sale_goods = models.CharField(max_length=255, verbose_name="折扣商品", blank=True,
                                  help_text="商品ID,商品ID,几率;...(没有则不填)")

    turntable_3 = models.CharField(max_length=255, verbose_name="3星天赋", blank=True,
                                      help_text="天赋ID,...(没有则不填)")
    turntable_6 = models.CharField(max_length=255, verbose_name="6星天赋", blank=True,
                                    help_text="天赋ID,...(没有则不填)")
    turntable_9 = models.CharField(max_length=255, verbose_name="9星天赋", blank=True,
                                     help_text="天赋ID,...(没有则不填)")

    class Meta:
        db_table = 'tower_level'
        verbose_name = '层级'
        verbose_name_plural = '层级'

    @classmethod
    def patch_fixture(cls, fixture):
        def parse_star_reward(text):
            result = []
            for x in text.split(';'):
                if not x:
                    # 后面跟着一个;
                    continue

                _id, _amount = x.split(',')
                result.append((int(_id), int(_amount)))

            return result

        def parse_turntable(text):
            if not text:
                return []

            return [int(i) for i in text.split(',')]

        def parse_sale_goods(text):
            result = []
            for x in text.split(';'):
                if not x:
                    continue

                _id, _amount, _prob  = x.split(',')
                result.append([int(_id), int(_amount), int(_prob)])

            for i in range(1, len(result)):
                result[i][2] += result[i-1][2]

            return result


        for f in fixture:
            staffs = []
            for staff in f['fields']['staffs'].split(';'):
                pos, staff_id, unit_id = staff.split(',')
                staffs.append([int(pos), int(staff_id), int(unit_id)])
            f['fields']['staffs'] = staffs

            star_reward = {
                '1': parse_star_reward(f['fields']['star_reward_1']),
                '2': parse_star_reward(f['fields']['star_reward_2']),
                '3': parse_star_reward(f['fields']['star_reward_3']),
            }

            f['fields'].pop('star_reward_1')
            f['fields'].pop('star_reward_2')
            f['fields'].pop('star_reward_3')

            f['fields']['star_reward'] = star_reward

            f['fields']['sale_goods'] = parse_sale_goods(f['fields']['sale_goods'])

            turntable = {
                '3': parse_turntable(f['fields']['turntable_3']),
                '6': parse_turntable(f['fields']['turntable_6']),
                '9': parse_turntable(f['fields']['turntable_9']),
            }

            f['fields'].pop('turntable_3')
            f['fields'].pop('turntable_6')
            f['fields'].pop('turntable_9')

            f['fields']['turntable'] = turntable

        return fixture


class TowerResetCost(models.Model):
    id = models.IntegerField(primary_key=True)
    cost = models.IntegerField(verbose_name="消耗钻石")

    class Meta:
        db_table = 'tower_reset_cost'
        verbose_name = '重置消耗'
        verbose_name_plural = '重置消耗'