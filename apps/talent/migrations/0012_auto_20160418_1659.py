# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0011_auto_20160418_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='image',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'\xe5\xa4\xa9\xe8\xb5\x8b\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='up_need',
            field=models.CharField(blank=True, help_text=b'ID,Number;ID,Number...', max_length=255, verbose_name=b'\xe6\xb6\x88\xe8\x80\x97\xe7\x89\xa9\xe5\x93\x81'),
        ),
    ]