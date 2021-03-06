# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0011_auto_20160524_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='des',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='guide',
            name='icon',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='guide',
            name='position',
            field=models.IntegerField(choices=[(1, b'\xe5\xb7\xa6'), (2, b'\xe5\x8f\xb3')], default=1),
        ),
        migrations.AlterField(
            model_name='guide',
            name='operate_type',
            field=models.IntegerField(choices=[(0, b'\xe7\xa9\xba\xe6\x93\x8d\xe4\xbd\x9c'), (1, b'\xe7\x82\xb9\xe5\x87\xbbUI'), (2, b'\xe6\x8b\x96\xe5\x8a\xa8UI'), (3, b'\xe7\x82\xb9\xe5\x87\xbb\xe5\xbb\xba\xe7\xad\x91'), (4, b'\xe6\x8b\x96\xe5\x8a\xa8\xe9\x98\xb5\xe5\x9e\x8b')], verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]
