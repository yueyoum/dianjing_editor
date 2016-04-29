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
    item = models.IntegerField(verbose_name="物品ID")
    tp = models.IntegerField(choices=GoodsType, verbose_name="物品类别")
    tp_icon = models.CharField(max_length=255, verbose_name="类别icon")
    price = models.IntegerField(verbose_name="商品价格")
    sale = models.IntegerField(blank=True, verbose_name="促销价", help_text="非促销商品不填")
    vip_need = models.IntegerField(blank=True, verbose_name="促销价所需vip等级",
                                   help_text="非促销商品不填")
    num = models.IntegerField(verbose_name="促销数量")
    des = models.CharField(max_length=255, blank=True, verbose_name="促销描述")

    class Meta:
        db_table = 'tower_sale_goods'
        verbose_name = '促销商品'
        verbose_name_plural = '促销商品'


class TowerStarReward(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="星级奖励")
    star = models.IntegerField(verbose_name="所需星数")
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
                _id, _amount = reward.split(',')
                rewards.append([int(_id), int(_amount)])
            f['fields']['reward'] = rewards


class TowerRankReward(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="爬塔奖励ID")
    rank_cap = models.IntegerField(verbose_name="排名区间上限")
    rank_floor = models.IntegerField(verbose_name="排名区间下限")
    reward = models.CharField(max_length=255, verbose_name="排名奖励", help_text="物品ID,数量;物品ID,数量")
    mail_sender = models.CharField(max_length=32, verbose_name="邮件ID")

    class Meta:
        db_table = 'tower_rank_reward'
        verbose_name = '爬塔奖励'
        verbose_name_plural = '爬塔奖励'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            rewards = []
            for reward in f['fields']['reward'].split(';'):
                _id, _amount = reward.split(',')
                rewards.append([int(_id), int(_amount)])
            f['fields']['reward'] = rewards


class TowerGameLevel(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="层级ID")
    name = models.CharField(max_length=32, verbose_name="层级名")
    buff = models.IntegerField(verbose_name="副本效果")
    npc_path = models.CharField(max_length=255, verbose_name="npc配置",
                                help_text="位置,选手ID,兵种ID;位置,选手ID,兵种ID(位置范围0~29)")
    star_one = models.CharField(max_length=255, verbose_name="1星奖励",
                                help_text="物品ID,数量;物品ID,数量...")
    star_two = models.CharField(max_length=255, verbose_name="2星奖励",
                                help_text="物品ID,数量;物品ID,数量...")
    star_three = models.CharField(max_length=255, verbose_name="3星奖励",
                                  help_text="物品ID,数量;物品ID,数量...")
    sale_goods = models.CharField(max_length=255, verbose_name="折扣商品", blank=True,
                                  help_text="普通商品ID,高级商品ID;...(没有则不填)")
    roulette_three = models.CharField(max_length=32, verbose_name="3星天赋", blank=True,
                                      help_text="天赋ID,概率;...(没有则不填)")
    roulette_six = models.CharField(max_length=32, verbose_name="6星天赋", blank=True,
                                    help_text="天赋ID,概率;...(没有则不填)")
    roulette_nine = models.CharField(max_length=32, verbose_name="9星天赋", blank=True,
                                     help_text="天赋ID,概率;...(没有则不填)")

    class Meta:
        db_table = 'tower_level'
        verbose_name = '层级'
        verbose_name_plural = '层级'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            npc_path = []
            for path in f['fields']['npc_path'].split(';'):
                slot, staff, unit = path.split(',')
                npc_path.append([int(slot), int(staff), int(unit)])
            f['fields']['npc_path'] = npc_path

            star_one = []
            for one in f['fields']['star_one'].split(';'):
                _id,  amount = one.split(',')
                star_one.append([int(_id), int(amount)])
            f['fields']['star_one'] = star_one

            star_two = []
            for two in f['fields']['star_two'].split(';'):
                _id, amount = two.split(',')
                star_two.append([int(_id), int(amount)])
            f['fields']['star_one'] = star_two

            star_three = []
            for three in f['fields']['star_three'].split(';'):
                _id, amount = three.split(',')
                star_three.append([int(_id), int(amount)])
            f['fields']['star_one'] = star_three

            if f['fields'].get('sale_goods', ""):
                sale_goods = []
                for goods in f['fields']['sale_goods'].split(';'):
                    id_one, id_two = goods.split(',')
                    sale_goods.append([int(id_one), int(id_two)])
                f['fields']['sale_goods'] = sale_goods

            if f['fields'].get('roulette_three', ""):
                roulette_three = []
                for buff in f['fields']['roulette_three'].split(';'):
                    _id, _range = buff.split(',')
                    roulette_three.append([int(_id), int(_range)])
                f['fields']['roulette_three'] = roulette_three

            if f['fields'].get('roulette_six', ""):
                roulette_six = []
                for buff in f['fields']['roulette_six'].split(';'):
                    _id, _range = buff.split(',')
                    roulette_six.append([int(_id), int(_range)])
                f['fields']['roulette_three'] = roulette_six

            if f['fields'].get('roulette_nine', ""):
                roulette_nine = []
                for buff in f['fields']['roulette_nine'].split(';'):
                    _id, _range = buff.split(',')
                    roulette_nine.append([int(_id), int(_range)])
                f['fields']['roulette_three'] = roulette_nine


class TowerResetCost(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="爬塔重置ID")
    times = models.IntegerField(verbose_name="第几次购买")
    cost = models.IntegerField(verbose_name="消耗钻石")

    class Meta:
        db_table = 'tower_reset_cost'
        verbose_name = '重置消耗'
        verbose_name_plural = '重置消耗'