# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 10:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('territory', '0003_inspirecost_reporttemplate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='territorybuilding',
            name='building_name',
        ),
    ]
