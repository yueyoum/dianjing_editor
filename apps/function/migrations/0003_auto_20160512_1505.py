# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 07:05
from __future__ import unicode_literals

from django.db import migrations


def change_null_to_0(apps, scheme_editor):
    Model = apps.get_module("function", "Function")
    Model.objects.filter(belong_to_building=None).update(belong_to_building=0)


class Migration(migrations.Migration):

    dependencies = [
        ('function', '0002_function_need_challenge_id'),
    ]

    operations = [
        migrations.RunPython(change_null_to_0)
    ]
