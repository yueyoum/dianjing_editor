# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_auto_20160105_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='lilun',
            field=models.PositiveIntegerField(default=0, help_text=b'\xe8\xa3\x85\xe5\xa4\x87\xe9\x9c\x80\xe8\xa6\x81\xe5\xa1\xab\xe5\x86\x99', verbose_name=b'\xe7\x90\x86\xe8\xae\xba'),
        ),
        migrations.AlterField(
            model_name='item',
            name='luoji',
            field=models.PositiveIntegerField(default=0, help_text=b'\xe8\xa3\x85\xe5\xa4\x87\xe9\x9c\x80\xe8\xa6\x81\xe5\xa1\xab\xe5\x86\x99', verbose_name=b'\xe9\x80\xbb\xe8\xbe\x91'),
        ),
        migrations.AlterField(
            model_name='item',
            name='meili',
            field=models.PositiveIntegerField(default=0, help_text=b'\xe8\xa3\x85\xe5\xa4\x87\xe9\x9c\x80\xe8\xa6\x81\xe5\xa1\xab\xe5\x86\x99', verbose_name=b'\xe9\xad\x85\xe5\x8a\x9b'),
        ),
        migrations.AlterField(
            model_name='item',
            name='minjie',
            field=models.PositiveIntegerField(default=0, help_text=b'\xe8\xa3\x85\xe5\xa4\x87\xe9\x9c\x80\xe8\xa6\x81\xe5\xa1\xab\xe5\x86\x99', verbose_name=b'\xe6\x95\x8f\xe6\x8d\xb7'),
        ),
        migrations.AlterField(
            model_name='item',
            name='wuxing',
            field=models.PositiveIntegerField(default=0, help_text=b'\xe8\xa3\x85\xe5\xa4\x87\xe9\x9c\x80\xe8\xa6\x81\xe5\xa1\xab\xe5\x86\x99', verbose_name=b'\xe6\x82\x9f\xe6\x80\xa7'),
        ),
    ]
