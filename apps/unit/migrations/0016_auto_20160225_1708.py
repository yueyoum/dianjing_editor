# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-25 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0015_unitnew_crit_multiple'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitnew',
            name='attack_tp',
            field=models.IntegerField(choices=[(1, b'\xe7\x89\xa9\xe7\x90\x86\xe6\x94\xbb\xe5\x87\xbb'), (2, b'\xe8\x83\xbd\xe9\x87\x8f\xe6\x94\xbb\xe5\x87\xbb'), (3, b'\xe7\x88\x86\xe7\x82\xb8\xe6\x94\xbb\xe5\x87\xbb')], verbose_name=b'\xe6\x94\xbb\xe5\x87\xbb\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='unitnew',
            name='defense_tp',
            field=models.IntegerField(choices=[(1, b'\xe7\x94\x9f\xe7\x89\xa9\xe6\x8a\xa4\xe7\x94\xb2'), (2, b'\xe8\x83\xbd\xe9\x87\x8f\xe6\x8a\xa4\xe7\x94\xb2'), (3, b'\xe6\x9c\xba\xe6\xa2\xb0\xe6\x8a\xa4\xe7\x94\xb2')], verbose_name=b'\xe9\x98\xb2\xe5\xbe\xa1\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]