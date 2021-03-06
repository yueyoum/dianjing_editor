# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0016_auto_20160119_1644'),
        ('match', '0023_auto_20160127_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingMatchScoreStore',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('times_limit', models.IntegerField(default=-1, help_text=b'-1\xe4\xb8\xba\xe6\xb2\xa1\xe6\x9c\x89\xe9\x99\x90\xe5\x88\xb6\xef\xbc\x8c0\xe4\xb8\xba\xe6\x97\xa0\xe6\xb3\x95\xe5\x85\x91\xe6\x8d\xa2\xef\xbc\x8c\xe6\xad\xa3\xe6\x95\xb4\xe6\x95\xb0N\xe8\xa1\xa8\xe7\xa4\xba\xe5\x8f\xaf\xe4\xbb\xa5\xe5\x85\x91\xe6\x8d\xa2N\xe6\xac\xa1', verbose_name=b'\xe6\xac\xa1\xe6\x95\xb0\xe9\x99\x90\xe5\x88\xb6')),
                ('score', models.IntegerField(verbose_name=b'\xe6\x89\x80\xe9\x9c\x80\xe7\xa7\xaf\xe5\x88\x86')),
                ('item_amount', models.IntegerField(default=1, verbose_name=b'\xe7\x89\xa9\xe5\x93\x81\xe6\x95\xb0\xe9\x87\x8f')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item', verbose_name=b'\xe7\x89\xa9\xe5\x93\x81')),
            ],
            options={
                'db_table': 'training_match_score_store',
                'verbose_name': '\u8bad\u7ec3\u8d5b\u79ef\u5206\u5546\u5e97',
                'verbose_name_plural': '\u8bad\u7ec3\u8d5b\u79ef\u5206\u5546\u5e97',
            },
        ),
    ]
