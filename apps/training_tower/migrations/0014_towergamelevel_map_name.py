# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_tower', '0013_auto_20160607_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='towergamelevel',
            name='map_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
