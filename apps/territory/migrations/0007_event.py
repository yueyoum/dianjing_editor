# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territory', '0006_territorystore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('target_exp', models.IntegerField(verbose_name='\u88ab\u5e2e\u52a9\u4eba\u83b7\u5f97\u7ecf\u9a8c')),
                ('reward_win', models.TextField(verbose_name='\u5e2e\u52a9\u4eba\u80dc\u5229\u83b7\u5f97\u8d44\u6e90')),
                ('reward_lose', models.TextField(verbose_name='\u5e2e\u52a9\u4eba\u5931\u8d25\u83b7\u5f97\u8d44\u6e90')),
                ('npc', models.IntegerField()),
                ('des', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'territory_event',
                'verbose_name': '\u968f\u673a\u4e8b\u4ef6',
                'verbose_name_plural': '\u968f\u673a\u4e8b\u4ef6',
            },
        ),
    ]
