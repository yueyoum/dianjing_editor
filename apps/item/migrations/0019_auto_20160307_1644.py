# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-07 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0018_auto_20160307_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentlevel',
            name='update_item_need',
            field=models.CharField(blank=True, help_text=b'id,\xe6\x95\xb0\xe9\x87\x8f;id,\xe6\x95\xb0\xe9\x87\x8f...', max_length=255, verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe9\x81\x93\xe5\x85\xb7'),
        ),
    ]