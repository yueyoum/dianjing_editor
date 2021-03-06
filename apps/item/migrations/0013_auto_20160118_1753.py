# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0012_auto_20160108_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='item.Item')),
                ('need_club_level', models.IntegerField(default=0, help_text=b'0 \xe8\xa1\xa8\xe7\xa4\xba\xe6\xb2\xa1\xe6\x9c\x89\xe9\x99\x90\xe5\x88\xb6', verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe6\x89\x80\xe9\x9c\x80\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe7\xad\x89\xe7\xba\xa7')),
                ('luoji', models.PositiveIntegerField(default=0, verbose_name=b'\xe9\x80\xbb\xe8\xbe\x91')),
                ('minjie', models.PositiveIntegerField(default=0, verbose_name=b'\xe6\x95\x8f\xe6\x8d\xb7')),
                ('lilun', models.PositiveIntegerField(default=0, verbose_name=b'\xe7\x90\x86\xe8\xae\xba')),
                ('wuxing', models.PositiveIntegerField(default=0, verbose_name=b'\xe6\x82\x9f\xe6\x80\xa7')),
                ('meili', models.PositiveIntegerField(default=0, verbose_name=b'\xe9\xad\x85\xe5\x8a\x9b')),
                ('template_1', models.CharField(help_text=b'\xe5\xb1\x9e\xe6\x80\xa7:\xe4\xb8\x8b\xe9\x99\x90~\xe4\xb8\x8a\xe9\x99\x90,\xe5\xb1\x9e\xe6\x80\xa7:\xe4\xb8\x8b\xe9\x99\x90~\xe4\xb8\x8a\xe9\x99\x90', max_length=255, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe6\xa8\xa1\xe6\x9d\xbf1')),
                ('template_2', models.CharField(help_text=b'\xe5\xb1\x9e\xe6\x80\xa7:\xe4\xb8\x8b\xe9\x99\x90~\xe4\xb8\x8a\xe9\x99\x90,\xe5\xb1\x9e\xe6\x80\xa7:\xe4\xb8\x8b\xe9\x99\x90~\xe4\xb8\x8a\xe9\x99\x90', max_length=255, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe6\xa8\xa1\xe6\x9d\xbf1')),
            ],
            options={
                'db_table': 'equipment',
                'verbose_name': '\u88c5\u5907',
                'verbose_name_plural': '\u88c5\u5907',
            },
        ),
        migrations.RemoveField(
            model_name='item',
            name='lilun',
        ),
        migrations.RemoveField(
            model_name='item',
            name='luoji',
        ),
        migrations.RemoveField(
            model_name='item',
            name='meili',
        ),
        migrations.RemoveField(
            model_name='item',
            name='minjie',
        ),
        migrations.RemoveField(
            model_name='item',
            name='wuxing',
        ),
    ]
