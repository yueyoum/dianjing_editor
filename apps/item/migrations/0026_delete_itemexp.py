# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 09:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0025_auto_20160411_1618'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemExp',
        ),
    ]
