# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-28 02:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qianban', '0010_auto_20161028_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspireleveladdition',
            name='level',
        ),
        migrations.RemoveField(
            model_name='inspirestepaddition',
            name='step',
        ),
    ]
