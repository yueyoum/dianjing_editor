# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qianban', '0006_auto_20151223_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='qianban',
            name='story_des',
            field=models.TextField(blank=True, verbose_name=b'\xe8\x83\x8c\xe6\x99\xaf\xe6\x95\x85\xe4\xba\x8b'),
        ),
    ]
