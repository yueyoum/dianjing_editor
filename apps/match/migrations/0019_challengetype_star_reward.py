# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0018_elitearea_star_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengetype',
            name='star_reward',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe6\x98\x9f\xe7\xba\xa7\xe5\xa5\x96\xe5\x8a\xb1'),
            preserve_default=False,
        ),
    ]
