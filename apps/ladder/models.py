# -*- coding: utf-8 -*-

from django.db import models

class LadderLogTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    template = models.CharField(max_length=255, verbose_name="模板")

    class Meta:
        db_table = 'ladder_log_template'
        verbose_name = '天梯战况模板'
        verbose_name_plural = '天梯战况模板'


class LadderRankReward(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="排名上限")
    name = models.CharField(max_length=255)
    reward_gold = models.IntegerField(default=0, verbose_name="奖励软妹币")
    reward_score = models.IntegerField(default=0, verbose_name="奖励积分")
    reward_des = models.TextField(verbose_name="奖励描述")
    mail_title = models.TextField(verbose_name="邮件标题")
    mail_content = models.TextField(verbose_name="邮件内容")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'ladder_rank_reward'
        verbose_name = "天梯排名奖励"
        verbose_name_plural = "天梯排名奖励"


class LadderScoreStore(models.Model):
    id = models.IntegerField(primary_key=True)
    times_limit = models.IntegerField(default=-1, verbose_name="次数限制",
                                      help_text="-1为没有限制，0为无法兑换，正整数N表示可以兑换N次")

    score = models.IntegerField(verbose_name="所需积分")

    item = models.ForeignKey('item.Item', verbose_name='物品')
    item_amount = models.IntegerField(default=1, verbose_name='物品数量')

    class Meta:
        db_table = 'ladder_score_store'
        verbose_name = "天梯积分商店"
        verbose_name_plural = "天梯积分商店"
