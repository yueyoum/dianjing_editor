# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0019_challengetype_star_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengetype',
            name='star_reward',
            field=models.CharField(default=b'1:2,2:3,5:6', max_length=255, verbose_name=b'\xe6\x98\x9f\xe7\xba\xa7\xe5\xa5\x96\xe5\x8a\xb1'),
        ),
    ]