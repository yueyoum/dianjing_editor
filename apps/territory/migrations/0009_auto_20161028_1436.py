# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-28 06:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('territory', '0008_event_resource'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InspireCost',
            new_name='TerritoryInspireCost',
        ),
        migrations.RenameModel(
            old_name='Inspire',
            new_name='Territorynspire',
        ),
    ]
