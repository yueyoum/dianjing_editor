# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0036_challengebuycost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Maps',
        ),
        migrations.AddField(
            model_name='challengechapter',
            name='map_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
