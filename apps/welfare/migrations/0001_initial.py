# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WelfareLevelReward',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
                ('reward', models.TextField(help_text='id,amount;id,amount;')),
            ],
            options={
                'db_table': 'welfare_level_reward',
                'verbose_name': '\u7b49\u7ea7\u793c\u5305',
                'verbose_name_plural': '\u7b49\u7ea7\u793c\u5305',
            },
        ),
        migrations.CreateModel(
            name='WelfareNewPlayer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('day', models.IntegerField()),
                ('reward', models.TextField(help_text='id,amount;id,amount;')),
            ],
            options={
                'db_table': 'welfare_new_player',
                'verbose_name': '\u65b0\u624b\u793c\u5305',
                'verbose_name_plural': '\u65b0\u624b\u793c\u5305',
            },
        ),
        migrations.CreateModel(
            name='WelfareSignIn',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('reward', models.TextField(help_text='id,amount;id,amount;')),
                ('vip', models.IntegerField()),
                ('vip_name', models.CharField(max_length=255)),
                ('vip_reward', models.TextField(help_text='id,amount;id,amount;')),
            ],
            options={
                'db_table': 'welfare_signin',
                'verbose_name': '\u7b7e\u5230\u5956\u52b1',
                'verbose_name_plural': '\u7b7e\u5230\u5956\u52b1',
            },
        ),
    ]
