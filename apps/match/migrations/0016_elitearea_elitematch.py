# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_clublevel_max_staff_amount'),
        ('unit', '0004_policy_icon'),
        ('package', '0010_package_items'),
        ('match', '0015_trainingmatchreward'),
    ]

    operations = [
        migrations.CreateModel(
            name='EliteArea',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('need_club_level', models.IntegerField(verbose_name=b'\xe6\x89\x80\xe9\x9c\x80\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe7\xad\x89\xe7\xba\xa7')),
                ('match_ids', models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe5\x85\xb3\xe5\x8d\xa1ID\xe5\x88\x97\xe8\xa1\xa8')),
                ('map_name', models.CharField(max_length=255, verbose_name=b'\xe5\x9c\xb0\xe5\x9b\xbe')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'db_table': 'elite_area',
                'verbose_name': '\u7cbe\u82f1\u8d5b\u5927\u533a',
                'verbose_name_plural': '\u7cbe\u82f1\u8d5b\u5927\u533a',
            },
        ),
        migrations.CreateModel(
            name='EliteMatch',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('max_times', models.IntegerField(verbose_name=b'\xe6\xac\xa1\xe6\x95\xb0\xe9\x99\x90\xe5\x88\xb6')),
                ('club_name', models.CharField(max_length=255, verbose_name=b'\xe5\x85\xb3\xe5\x8d\xa1\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe5\x90\x8d\xe5\xad\x97')),
                ('staff_level', models.IntegerField(verbose_name=b'\xe9\x80\x89\xe6\x89\x8b\xe7\xad\x89\xe7\xba\xa7')),
                ('staffs', models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe9\x80\x89\xe6\x89\x8bID\xe5\x88\x97\xe8\xa1\xa8')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('club_flag', models.ForeignKey(verbose_name=b'\xe5\x85\xb3\xe5\x8d\xa1\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe6\x97\x97\xe5\xb8\x9c', to='club.ClubFlag')),
                ('policy', models.ForeignKey(verbose_name=b'\xe6\x88\x98\xe6\x9c\xaf', to='unit.Policy')),
                ('reward', models.ForeignKey(verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1\xe7\x89\xa9\xe5\x93\x81\xe5\x8c\x85', to='package.Package')),
            ],
            options={
                'db_table': 'elite_match',
                'verbose_name': '\u7cbe\u82f1\u8d5b\u5c0f\u5173\u5361',
                'verbose_name_plural': '\u7cbe\u82f1\u8d5b\u5c0f\u5173',
            },
        ),
    ]
