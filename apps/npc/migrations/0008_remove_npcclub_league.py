# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 02:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('npc', '0007_auto_20151223_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='npcclub',
            name='league',
        ),
    ]