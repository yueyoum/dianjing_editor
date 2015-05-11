# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NPCClub',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe5\x90\x8d\xe5\xad\x97')),
                ('manager_name', models.CharField(max_length=32, verbose_name=b'\xe7\xbb\x8f\xe7\x90\x86\xe4\xba\xba\xe5\x90\x8d\xe5\xad\x97')),
                ('jingong_low', models.IntegerField(verbose_name=b'\xe8\xbf\x9b\xe6\x94\xbb\xe4\xb8\x8b\xe9\x99\x90')),
                ('jingong_high', models.FloatField(verbose_name=b'\xe8\xbf\x9b\xe6\x94\xbb\xe4\xb8\x8a\xe9\x99\x90')),
                ('qianzhi_low', models.IntegerField(verbose_name=b'\xe7\x89\xb5\xe5\x88\xb6\xe4\xb8\x8b\xe9\x99\x90')),
                ('qianzhi_high', models.FloatField(verbose_name=b'\xe7\x89\xb5\xe5\x88\xb6\xe4\xb8\x8a\xe9\x99\x90')),
                ('xintai_low', models.IntegerField(verbose_name=b'\xe5\xbf\x83\xe6\x80\x81\xe4\xb8\x8b\xe9\x99\x90')),
                ('xintai_high', models.FloatField(verbose_name=b'\xe5\xbf\x83\xe6\x80\x81\xe4\xb8\x8a\xe9\x99\x90')),
                ('baobing_low', models.IntegerField(verbose_name=b'\xe6\x9a\xb4\xe5\x85\xb5\xe4\xb8\x8b\xe9\x99\x90')),
                ('baobing_high', models.FloatField(verbose_name=b'\xe6\x9a\xb4\xe5\x85\xb5\xe4\xb8\x8a\xe9\x99\x90')),
                ('fangshou_low', models.IntegerField(verbose_name=b'\xe9\x98\xb2\xe5\xae\x88\xe4\xb8\x8b\xe9\x99\x90')),
                ('fangshou_high', models.FloatField(verbose_name=b'\xe9\x98\xb2\xe5\xae\x88\xe4\xb8\x8a\xe9\x99\x90')),
                ('yunying_low', models.IntegerField(verbose_name=b'\xe8\xbf\x90\xe8\x90\xa5\xe4\xb8\x8b\xe9\x99\x90')),
                ('yunying_high', models.FloatField(verbose_name=b'\xe8\xbf\x90\xe8\x90\xa5\xe4\xb8\x8a\xe9\x99\x90')),
                ('yishi_low', models.IntegerField(verbose_name=b'\xe6\x84\x8f\xe8\xaf\x86\xe4\xb8\x8b\xe9\x99\x90')),
                ('yishi_high', models.FloatField(verbose_name=b'\xe6\x84\x8f\xe8\xaf\x86\xe4\xb8\x8a\xe9\x99\x90')),
                ('caozuo_low', models.IntegerField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe4\xb8\x8b\xe9\x99\x90')),
                ('caozuo_high', models.FloatField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe4\xb8\x8a\xe9\x99\x90')),
            ],
            options={
                'db_table': 'npc_club',
                'verbose_name': 'NPC\u4ff1\u4e50\u90e8',
                'verbose_name_plural': 'NPC\u4ff1\u4e50\u90e8',
            },
        ),
    ]
