# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_tower', '0003_auto_20160429_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='towergamelevel',
            name='sale_goods',
            field=models.CharField(blank=True, help_text='\u666e\u901a\u5546\u54c1ID,\u9ad8\u7ea7\u5546\u54c1ID;...(\u6ca1\u6709\u5219\u4e0d\u586b)', max_length=255, verbose_name='\u6298\u6263\u5546\u54c1'),
        ),
        migrations.AlterField(
            model_name='towersalegoods',
            name='tp',
            field=models.IntegerField(choices=[(1, '\u666e\u901a\u5546\u54c1'), (2, '\u9ad8\u7ea7\u5546\u54c1')], verbose_name='\u7269\u54c1\u7c7b\u522b'),
        ),
    ]
