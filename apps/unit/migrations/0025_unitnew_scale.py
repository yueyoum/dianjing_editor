# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0024_auto_20160411_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitnew',
            name='scale',
            field=models.FloatField(default=1, verbose_name=b'\xe7\xbc\xa9\xe6\x94\xbe'),
        ),
    ]
