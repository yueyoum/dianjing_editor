# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-21 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VIP',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('update_vip_exp', models.IntegerField()),
                ('item_id', models.IntegerField(verbose_name='\u793c\u5305ID')),
                ('diamond_original', models.IntegerField(verbose_name='\u94bb\u77f3\u539f\u4ef7')),
                ('diamond_now', models.IntegerField(verbose_name='\u94bb\u77f3\u73b0\u4ef7')),
                ('item_preview', models.TextField(verbose_name='\u793c\u5305\u9884\u89c8')),
                ('des', models.TextField()),
            ],
            options={
                'db_table': 'vip',
                'verbose_name': 'VIP',
                'verbose_name_plural': 'VIP',
            },
        ),
    ]