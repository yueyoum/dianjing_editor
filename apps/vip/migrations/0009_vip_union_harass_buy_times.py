# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0008_auto_20160902_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='vip',
            name='union_harass_buy_times',
            field=models.IntegerField(default=0, verbose_name='\u516c\u4f1a\u9a9a\u6270\u8d2d\u4e70\u6b21\u6570'),
        ),
    ]
