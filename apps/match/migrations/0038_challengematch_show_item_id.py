# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0037_auto_20160617_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengematch',
            name='show_item_id',
            field=models.IntegerField(default=0),
        ),
    ]