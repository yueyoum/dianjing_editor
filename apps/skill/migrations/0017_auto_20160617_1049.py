# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0016_auto_20160414_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='buff',
            name='icon',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buff',
            name='mode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
