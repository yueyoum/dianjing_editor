# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_tower', '0006_auto_20160506_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='towerrankreward',
            name='mail_sender',
        ),
        migrations.AddField(
            model_name='towerrankreward',
            name='mail_content',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='towerrankreward',
            name='mail_title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
