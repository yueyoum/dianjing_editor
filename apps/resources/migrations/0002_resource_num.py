# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
