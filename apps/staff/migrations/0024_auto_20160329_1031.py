# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-29 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0023_auto_20160329_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffnew',
            name='operation',
            field=models.IntegerField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c'),
        ),
    ]
