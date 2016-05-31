# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dungeon', '0007_delete_dungeonbuycost'),
    ]

    operations = [
        migrations.CreateModel(
            name='DungeonResetCost',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dungeon_id', models.IntegerField()),
                ('reset_times', models.IntegerField()),
                ('diamond', models.IntegerField(verbose_name='\u94bb\u77f3')),
            ],
            options={
                'db_table': 'dungeon_reset_cost',
                'verbose_name': '\u526f\u672c\u91cd\u7f6e\u82b1\u8d39',
                'verbose_name_plural': '\u526f\u672c\u91cd\u7f6e\u82b1\u8d39',
            },
        ),
    ]
