# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-11 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0016_auto_20160225_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitnew',
            name='effect_die',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe6\xad\xbb\xe4\xba\xa1\xe7\x89\xb9\xe6\x95\x88'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unitnew',
            name='effect_move',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x89\xb9\xe6\x95\x88'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unitnew',
            name='effect_skill_1',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe6\x99\xae\xe6\x94\xbb\xe5\x8a\xa8\xe4\xbd\x9c\xe7\x89\xb9\xe6\x95\x88'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unitnew',
            name='effect_skill_2',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd\xe5\x8a\xa8\xe4\xbd\x9c\xe7\x89\xb9\xe6\x95\x88'),
            preserve_default=False,
        ),
    ]
