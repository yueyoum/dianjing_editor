# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 05:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0015_auto_20160601_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talent',
            old_name='up_need_point',
            new_name='up_need',
        ),
        migrations.RemoveField(
            model_name='talent',
            name='up_need_items',
        ),
    ]
