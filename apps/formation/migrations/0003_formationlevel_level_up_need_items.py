# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0002_formation_formationlevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='formationlevel',
            name='level_up_need_items',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
