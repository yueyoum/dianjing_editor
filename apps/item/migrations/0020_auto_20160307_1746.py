# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-07 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0019_auto_20160307_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentlevel',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
