# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0010_auto_20160418_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='unlock',
            field=models.IntegerField(verbose_name=b'\xe5\x89\x8d\xe7\xbd\xae\xe6\x9d\xa1\xe4\xbb\xb6'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='up_need',
            field=models.CharField(help_text=b'ID,Number;ID,Number...', max_length=255, verbose_name=b'\xe6\xb6\x88\xe8\x80\x97\xe7\x89\xa9\xe5\x93\x81'),
        ),
    ]
