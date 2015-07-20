# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('attr_mode', models.IntegerField(default=1, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe6\xa8\xa1\xe5\xbc\x8f', choices=[(1, b'\xe4\xb8\x8d\xe5\x8a\xa0\xe6\x88\x90\xe5\xb1\x9e\xe6\x80\xa7'), (2, b'\xe5\xae\x8c\xe5\x85\xa8\xe9\x9a\x8f\xe6\x9c\xba'), (3, b'\xe4\xbb\x8e\xe8\xae\xbe\xe5\xae\x9a\xe7\x9a\x84\xe5\xb1\x9e\xe6\x80\xa7\xe4\xb8\xad\xe9\x9a\x8f\xe6\x9c\xba'), (4, b'\xe8\xae\xbe\xe5\xae\x9a\xe7\x9a\x84\xe5\xb1\x9e\xe6\x80\xa7')])),
                ('attr_random_amount', models.IntegerField(default=0, help_text=b'\xe5\x8f\xaa\xe6\x9c\x89 \xe5\xb1\x9e\xe6\x80\xa7\xe6\xa8\xa1\xe5\xbc\x8f \xe4\xb8\xba \xe9\x9a\x8f\xe6\x9c\xba \xe6\x97\xb6\xef\xbc\x8c\xe6\x89\x8d\xe6\x9c\x89\xe7\x94\xa8', verbose_name=b'\xe9\x9a\x8f\xe6\x9c\xba\xe5\xb1\x9e\xe6\x80\xa7\xe6\x95\xb0\xe9\x87\x8f')),
                ('attr_random_value', models.CharField(help_text=b'\xe5\x8f\xaa\xe6\x9c\x89 \xe5\xb1\x9e\xe6\x80\xa7\xe6\xa8\xa1\xe5\xbc\x8f \xe4\xb8\xba \xe5\xae\x8c\xe5\x85\xa8\xe9\x9a\x8f\xe6\x9c\xba \xe6\x97\xb6\xef\xbc\x8c\xe6\x89\x8d\xe6\x9c\x89\xe7\x94\xa8', max_length=32, verbose_name=b'\xe9\x9a\x8f\xe6\x9c\xba\xe7\x86\x9f\xe6\x82\x89\xe5\x80\xbc\xe8\x8c\x83\xe5\x9b\xb4', blank=True)),
                ('jingong', models.CharField(max_length=32, verbose_name=b'\xe8\xbf\x9b\xe6\x94\xbb', blank=True)),
                ('qianzhi', models.CharField(max_length=32, verbose_name=b'\xe7\x89\xb5\xe5\x88\xb6', blank=True)),
                ('xintai', models.CharField(max_length=32, verbose_name=b'\xe5\xbf\x83\xe6\x80\x81', blank=True)),
                ('baobing', models.CharField(max_length=32, verbose_name=b'\xe6\x9a\xb4\xe5\x85\xb5', blank=True)),
                ('fangshou', models.CharField(max_length=32, verbose_name=b'\xe9\x98\xb2\xe5\xae\x88', blank=True)),
                ('yunying', models.CharField(max_length=32, verbose_name=b'\xe8\xbf\x90\xe8\x90\xa5', blank=True)),
                ('yishi', models.CharField(max_length=32, verbose_name=b'\xe6\x84\x8f\xe8\xaf\x86', blank=True)),
                ('caozuo', models.CharField(max_length=32, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c', blank=True)),
                ('gold', models.CharField(max_length=32, verbose_name=b'\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81', blank=True)),
                ('diamond', models.CharField(max_length=32, verbose_name=b'\xe9\x92\xbb\xe7\x9f\xb3', blank=True)),
                ('staff_exp', models.CharField(max_length=32, verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5\xe7\xbb\x8f\xe9\xaa\x8c', blank=True)),
                ('club_renown', models.CharField(max_length=32, verbose_name=b'\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe5\xa3\xb0\xe6\x9c\x9b', blank=True)),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'db_table': 'package',
                'verbose_name': '\u7269\u54c1\u5305',
                'verbose_name_plural': '\u7269\u54c1\u5305',
            },
        ),
    ]
