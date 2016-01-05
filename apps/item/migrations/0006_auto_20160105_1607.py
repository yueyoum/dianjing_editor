# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20160105_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='lilun',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x90\x86\xe8\xae\xba'),
        ),
        migrations.AddField(
            model_name='item',
            name='luoji',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\x80\xbb\xe8\xbe\x91'),
        ),
        migrations.AddField(
            model_name='item',
            name='meili',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\xad\x85\xe5\x8a\x9b'),
        ),
        migrations.AddField(
            model_name='item',
            name='minjie',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x95\x8f\xe6\x8d\xb7'),
        ),
        migrations.AddField(
            model_name='item',
            name='sub_tp',
            field=models.IntegerField(choices=[(0, b'\xe6\x97\xa0\xe5\xad\x90\xe7\xb1\xbb\xe5\x9e\x8b'), (1, b'\xe5\xb0\x8f\xe5\x9e\x8b\xe8\xa3\x85\xe5\xa4\x87'), (2, b'\xe5\xa4\xa7\xe5\x9e\x8b\xe8\xa3\x85\xe5\xa4\x87'), (3, b'\xe4\xba\xba\xe7\x89\xa9\xe9\x85\x8d\xe9\xa5\xb0'), (4, b'\xe4\xbf\xa1\xe7\x89\xa9')], default=0, verbose_name=b'\xe5\xad\x90\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AddField(
            model_name='item',
            name='wuxing',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x82\x9f\xe6\x80\xa7'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tp',
            field=models.IntegerField(choices=[(1, b'\xe5\x9f\xb9\xe8\xae\xad\xe8\x80\x97\xe6\x9d\x90'), (2, b'\xe7\xbd\x91\xe5\xba\x97\xe8\xb4\xa7\xe7\x89\xa9'), (3, b'\xe5\xbb\xba\xe7\xad\x91\xe8\xae\xb8\xe5\x8f\xaf\xe8\xaf\x81'), (11, b'\xe8\xa3\x85\xe5\xa4\x87')], default=1, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]