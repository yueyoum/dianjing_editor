# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_auto_20170113_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalconfig',
            name='value_string',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='globalconfig',
            name='value',
            field=models.IntegerField(),
        ),
    ]
