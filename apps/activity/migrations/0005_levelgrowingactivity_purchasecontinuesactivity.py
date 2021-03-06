# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-22 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_auto_20170223_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelGrowingActivity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('des', models.TextField()),
                ('rewards', models.TextField()),
            ],
            options={
                'db_table': 'level_growing_activity',
                'verbose_name': '\u7b49\u7ea7\u6210\u957f\u6d3b\u52a8',
                'verbose_name_plural': '\u7b49\u7ea7\u6210\u957f\u6d3b\u52a8',
            },
        ),
        migrations.CreateModel(
            name='PurchaseContinuesActivity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('des', models.TextField()),
                ('rewards', models.TextField()),
            ],
            options={
                'db_table': 'purchase_continues_activity',
                'verbose_name': '\u8fde\u7eed\u5145\u503c\u6d3b\u52a8',
                'verbose_name_plural': '\u8fde\u7eed\u5145\u503c\u6d3b\u52a8',
            },
        ),
    ]
