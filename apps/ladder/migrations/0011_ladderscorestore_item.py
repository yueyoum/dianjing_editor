# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-11 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ladder', '0010_remove_ladderscorestore_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='ladderscorestore',
            name='item',
            field=models.IntegerField(default=0),
        ),
    ]