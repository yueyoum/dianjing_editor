# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_tower', '0011_auto_20160607_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='towergamelevel',
            name='sale_goods',
            field=models.CharField(blank=True, help_text='\u5546\u54c1ID,\u5546\u54c1ID,\u51e0\u7387;...(\u6ca1\u6709\u5219\u4e0d\u586b)', max_length=255, verbose_name='\u6298\u6263\u5546\u54c1'),
        ),
    ]