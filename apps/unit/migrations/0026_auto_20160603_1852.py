# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0025_unitnew_scale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitnew',
            name='race',
            field=models.IntegerField(verbose_name=b'\xe7\xa7\x8d\xe6\x97\x8f'),
        ),
    ]
