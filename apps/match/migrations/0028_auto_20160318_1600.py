# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-18 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0027_auto_20160318_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengematch',
            name='tp',
            field=models.IntegerField(choices=[(1, b'\xe6\x99\xae\xe9\x80\x9a'), (2, b'\xe7\xb2\xbe\xe8\x8b\xb1')], verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]
