# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20160523_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='storetype',
            name='show_refresh',
            field=models.BooleanField(default=True),
        ),
    ]