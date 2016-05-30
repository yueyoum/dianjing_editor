# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dungeon', '0005_auto_20160530_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='DungeonBuyCost',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u8d2d\u4e70\u6b21\u6570')),
                ('diamond', models.IntegerField(verbose_name='\u94bb\u77f3')),
            ],
            options={
                'db_table': 'dungeon_buy_cost',
                'verbose_name': '\u526f\u672c\u8d2d\u4e70\u82b1\u8d39',
                'verbose_name_plural': '\u526f\u672c\u8d2d\u4e70\u82b1\u8d39',
            },
        ),
    ]
