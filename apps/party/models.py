# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from misc import parse_text_split_by_comma, parse_text

class PartyLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    need_union_level = models.IntegerField()
    need_diamond = models.IntegerField()
    talent_skills = models.CharField(max_length=255)
    item_id = models.IntegerField()
    mail_title = models.TextField()
    mail_content = models.TextField()
    buy_one = models.IntegerField()
    buy_two = models.IntegerField()

    class Meta:
        db_table = 'party_level'
        verbose_name = '宴会等级'
        verbose_name_plural = '宴会等级'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['talent_skills'] = parse_text_split_by_comma(f['fields']['talent_skills'])

        return fixture


class PartyBuyItem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    reward = models.TextField()

    class Meta:
        db_table = 'party_buy_item'
        verbose_name = '宴会购买'
        verbose_name_plural = '宴会购买'

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['cost'] = parse_text(f['fields']['cost'], 2)
            f['fields']['reward'] = parse_text(f['fields']['reward'], 2)

        return fixture


class PartyMessageTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    template = models.TextField()

    class Meta:
        db_table = 'party_message_template'
        verbose_name = '宴会消息模板'
        verbose_name_plural = '宴会消息模板'
