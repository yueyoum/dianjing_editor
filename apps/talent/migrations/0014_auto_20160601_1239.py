# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0013_auto_20160420_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talent',
            old_name='up_need',
            new_name='up_need_point',
        ),
        migrations.AddField(
            model_name='talent',
            name='up_need_items',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\xb6\x88\xe8\x80\x97\xe9\x81\x93\xe5\x85\xb7'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='unlock',
            field=models.IntegerField(db_index=True, verbose_name=b'\xe5\x89\x8d\xe7\xbd\xae\xe6\x9d\xa1\xe4\xbb\xb6'),
        ),
    ]
