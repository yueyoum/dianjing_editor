# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-29 03:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0025_auto_20160329_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffnew',
            name='name',
        ),
        migrations.RemoveField(
            model_name='staffnew',
            name='picture',
        ),
    ]
