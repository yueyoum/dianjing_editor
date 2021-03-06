# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingSlot',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('building_id', models.IntegerField(db_index=True)),
                ('need_building_level', models.IntegerField()),
                ('need_vip_level', models.IntegerField()),
                ('exp_modulus', models.FloatField()),
            ],
            options={
                'db_table': 'territory_building_slot',
                'verbose_name': '\u5efa\u7b51\u683c\u5b50',
                'verbose_name_plural': '\u5efa\u7b51\u683c\u5b50',
            },
        ),
        migrations.CreateModel(
            name='BuildingSlotExtraProduct',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('slot_id', models.IntegerField(db_index=True)),
                ('building_level', models.IntegerField()),
                ('extra_product', models.TextField(help_text='id,amount;')),
                ('cost_amount', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'territory_building_slot_extra_product',
                'verbose_name': '\u683c\u5b50\u4ea7\u51fa',
                'verbose_name_plural': '\u683c\u5b50\u4ea7\u51fa',
            },
        ),
        migrations.CreateModel(
            name='StaffSpecialProduct',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_1', models.TextField(help_text='id,amount_low,amount_high;')),
                ('product_2', models.TextField(help_text='id,amount_low,amount_high;')),
                ('product_3', models.TextField(help_text='id,amount_low,amount_high;')),
            ],
            options={
                'db_table': 'territory_special_product',
                'verbose_name': '\u9009\u624b\u7279\u6b8a\u4ea7\u51fa',
                'verbose_name_plural': '\u9009\u624b\u7279\u6b8a\u4ea7\u51fa',
            },
        ),
        migrations.CreateModel(
            name='TerritoryBuilding',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('building_id', models.IntegerField()),
                ('building_name', models.CharField(max_length=32)),
                ('building_level', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('product_rate', models.IntegerField(verbose_name='\u6bcf\u5c0f\u65f6\u4ea7\u91cf')),
                ('events', models.CharField(max_length=255)),
                ('product_limit', models.IntegerField(verbose_name='\u8d44\u6e90\u4e0a\u9650')),
            ],
            options={
                'db_table': 'territory_building',
                'verbose_name': '\u9886\u5730\u5efa\u7b51',
                'verbose_name_plural': '\u9886\u5730\u5efa\u7b51',
            },
        ),
    ]
