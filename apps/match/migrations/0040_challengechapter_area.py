# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0039_auto_20160630_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengechapter',
            name='area',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
