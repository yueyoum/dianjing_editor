# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-18 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseStationLevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product', models.TextField()),
                ('exp', models.IntegerField()),
            ],
            options={
                'db_table': 'base_station_level',
                'verbose_name': '\u57fa\u5730\u7b49\u7ea7',
                'verbose_name_plural': '\u57fa\u5730\u7b49\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='PlunderBuyTimesCost',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cost', models.IntegerField()),
            ],
            options={
                'db_table': 'plunder_buy_times_cost',
                'verbose_name': '\u63a0\u593a\u8d2d\u4e70\u6b21\u6570\u82b1\u8d39',
                'verbose_name_plural': '\u63a0\u593a\u8d2d\u4e70\u6b21\u6570\u82b1\u8d39',
            },
        ),
        migrations.CreateModel(
            name='PlunderIncome',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u80dc\u51e0\u8def')),
                ('percent', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('extra_income', models.TextField()),
            ],
            options={
                'db_table': 'plunder_income',
                'verbose_name': '\u63a0\u593a\u6536\u76ca',
                'verbose_name_plural': '\u63a0\u593a\u6536\u76ca',
            },
        ),
    ]