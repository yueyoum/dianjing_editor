# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('avatar', models.CharField(max_length=32, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f')),
                ('nation', models.CharField(max_length=32, verbose_name=b'\xe5\x9b\xbd\xe7\xb1\x8d')),
                ('buy_cost', models.IntegerField(verbose_name=b'\xe7\xad\xbe\xe7\xba\xa6\xe8\xb4\xb9')),
                ('des', models.TextField(verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b', blank=True)),
                ('jingong', models.IntegerField(verbose_name=b'\xe8\xbf\x9b\xe6\x94\xbb')),
                ('jingong_grow', models.FloatField(verbose_name=b'\xe8\xbf\x9b\xe6\x94\xbb\xe6\x88\x90\xe9\x95\xbf')),
                ('qianzhi', models.IntegerField(verbose_name=b'\xe7\x89\xb5\xe5\x88\xb6')),
                ('qianzhi_grow', models.FloatField(verbose_name=b'\xe7\x89\xb5\xe5\x88\xb6\xe6\x88\x90\xe9\x95\xbf')),
                ('xintai', models.IntegerField(verbose_name=b'\xe5\xbf\x83\xe6\x80\x81')),
                ('xintai_grow', models.FloatField(verbose_name=b'\xe5\xbf\x83\xe6\x80\x81\xe6\x88\x90\xe9\x95\xbf')),
                ('baobing', models.IntegerField(verbose_name=b'\xe6\x9a\xb4\xe5\x85\xb5')),
                ('baobing_grow', models.FloatField(verbose_name=b'\xe6\x9a\xb4\xe5\x85\xb5\xe6\x88\x90\xe9\x95\xbf')),
                ('fangshou', models.IntegerField(verbose_name=b'\xe9\x98\xb2\xe5\xae\x88')),
                ('fangshou_grow', models.FloatField(verbose_name=b'\xe9\x98\xb2\xe5\xae\x88\xe6\x88\x90\xe9\x95\xbf')),
                ('yunying', models.IntegerField(verbose_name=b'\xe8\xbf\x90\xe8\x90\xa5')),
                ('yunying_grow', models.FloatField(verbose_name=b'\xe8\xbf\x90\xe8\x90\xa5\xe6\x88\x90\xe9\x95\xbf')),
                ('yishi', models.IntegerField(verbose_name=b'\xe6\x84\x8f\xe8\xaf\x86')),
                ('yishi_grow', models.FloatField(verbose_name=b'\xe6\x84\x8f\xe8\xaf\x86\xe6\x88\x90\xe9\x95\xbf')),
                ('caozuo', models.IntegerField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c')),
                ('caozuo_grow', models.FloatField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe6\x88\x90\xe9\x95\xbf')),
            ],
            options={
                'db_table': 'staff',
                'verbose_name': '\u5458\u5de5',
                'verbose_name_plural': '\u5458\u5de5',
            },
        ),
        migrations.CreateModel(
            name='StaffQuality',
            fields=[
                ('id', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('color', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'staff_quality',
                'verbose_name': '\u54c1\u8d28',
                'verbose_name_plural': '\u54c1\u8d28',
            },
        ),
        migrations.CreateModel(
            name='StaffRace',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'db_table': 'staff_race',
                'verbose_name': '\u79cd\u65cf',
                'verbose_name_plural': '\u79cd\u65cf',
            },
        ),
        migrations.CreateModel(
            name='StaffStatus',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('value', models.IntegerField(help_text=b'5% \xe7\x9b\xb4\xe6\x8e\xa5\xe5\xa1\xab5', verbose_name=b'\xe5\x8a\xa0\xe6\x88\x90\xe5\x80\xbc')),
            ],
            options={
                'db_table': 'staff_status',
                'verbose_name': '\u72b6\u6001',
                'verbose_name_plural': '\u72b6\u6001',
            },
        ),
        migrations.AddField(
            model_name='staff',
            name='quality',
            field=models.ForeignKey(db_column=b'quality', verbose_name=b'\xe5\x93\x81\xe8\xb4\xa8', to='staff.StaffQuality'),
        ),
        migrations.AddField(
            model_name='staff',
            name='race',
            field=models.ForeignKey(db_column=b'race', verbose_name=b'\xe7\xa7\x8d\xe6\x97\x8f', to='staff.StaffRace'),
        ),
    ]
