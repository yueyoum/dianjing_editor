# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-19 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plunder', '0002_plundernpc'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlunderDayReward',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('reward', models.TextField()),
            ],
            options={
                'db_table': 'plunder_day_reward',
                'verbose_name': '\u63a0\u593a\u6bcf\u65e5\u5956\u52b1',
                'verbose_name_plural': '\u63a0\u593a\u6bcf\u65e5\u5956\u52b1',
            },
        ),
    ]
