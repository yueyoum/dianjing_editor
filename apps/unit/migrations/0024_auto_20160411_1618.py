# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-11 08:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0033_auto_20160411_1618'),
        ('unit', '0023_auto_20160406_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='race',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='unitdes',
            name='policy',
        ),
        migrations.RemoveField(
            model_name='unitdes',
            name='unit',
        ),
        migrations.DeleteModel(
            name='UnitEffect',
        ),
        migrations.DeleteModel(
            name='Policy',
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
        migrations.DeleteModel(
            name='UnitDes',
        ),
    ]
