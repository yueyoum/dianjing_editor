# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-26 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0028_itemnew_sub_tp'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentSpecial',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('staff_attack', models.IntegerField()),
                ('staff_defense', models.IntegerField()),
                ('staff_manage', models.IntegerField()),
                ('staff_attack_percent', models.FloatField()),
                ('staff_defense_percent', models.FloatField()),
                ('staff_manage_percent', models.FloatField()),
                ('unit_attack_percent', models.FloatField(verbose_name=b'\xe6\x94\xbb\xe5\x87\xbb\xe7\x99\xbe\xe5\x88\x86\xe6\xaf\x94')),
                ('unit_defense_percent', models.FloatField(verbose_name=b'\xe9\x98\xb2\xe5\xbe\xa1\xe7\x99\xbe\xe5\x88\x86\xe6\xaf\x94')),
                ('unit_hp_percent', models.FloatField(verbose_name=b'\xe7\x94\x9f\xe5\x91\xbd\xe7\x99\xbe\xe5\x88\x86\xe6\xaf\x94')),
                ('unit_hit_rate', models.FloatField(verbose_name=b'\xe5\x91\xbd\xe4\xb8\xad\xe7\x8e\x87')),
                ('unit_dodge_rate', models.FloatField(verbose_name=b'\xe9\x97\xaa\xe9\x81\xbf\xe7\x8e\x87')),
                ('unit_crit_rate', models.FloatField(verbose_name=b'\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87')),
                ('unit_toughness_rate', models.FloatField(verbose_name=b'\xe9\x9f\xa7\xe6\x80\xa7')),
                ('unit_crit_multiple', models.FloatField(verbose_name=b'\xe6\x9a\xb4\xe5\x87\xbb\xe8\xa2\xab\xe7\x8e\x87')),
                ('unit_hurt_addition_to_terran', models.FloatField(verbose_name=b'\xe5\xaf\xb9\xe4\xba\xba\xe6\x97\x8f\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90')),
                ('unit_hurt_addition_to_protoss', models.FloatField(verbose_name=b'\xe5\xaf\xb9\xe7\xa5\x9e\xe6\x97\x8f\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90')),
                ('unit_hurt_addition_to_zerg', models.FloatField(verbose_name=b'\xe5\xaf\xb9\xe8\x99\xab\xe6\x97\x8f\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90')),
                ('unit_hurt_addition_by_terran', models.FloatField(verbose_name=b'\xe5\x8f\x97\xe5\x88\xb0\xe4\xba\xba\xe6\x97\x8f\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90')),
                ('unit_hurt_addition_by_protoss', models.FloatField(verbose_name=b'\xe5\x8f\x97\xe5\x88\xb0\xe7\xa5\x9e\xe6\x97\x8f\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90')),
                ('unit_hurt_addition_by_zerg', models.FloatField(verbose_name=b'\xe5\x8f\x97\xe5\x88\xb0\xe8\x99\xab\xe6\x97\x8f\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90')),
                ('skills', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'equipment_special',
                'verbose_name': '\u7279\u6b8a\u88c5\u5907',
                'verbose_name_plural': '\u7279\u6b8a\u88c5\u5907',
            },
        ),
        migrations.CreateModel(
            name='EquipmentSpecialGenerate',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('normal_cost', models.TextField()),
                ('normal_generate', models.TextField()),
                ('advance_cost', models.TextField()),
                ('advance_generate', models.TextField()),
                ('minutes', models.IntegerField()),
            ],
            options={
                'db_table': 'equipment_special_generate',
                'verbose_name': '\u7279\u6b8a\u88c5\u5907\u5236\u9020',
                'verbose_name_plural': '\u7279\u6b8a\u88c5\u5907\u5236\u9020',
            },
        ),
        migrations.CreateModel(
            name='EquipmentSpecialGrowingProperty',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('growing_low', models.IntegerField()),
                ('growing_high', models.IntegerField()),
                ('property_active_levels', models.CharField(blank=True, max_length=255)),
                ('skill_active_levels', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'equipment_special_growing_property',
                'verbose_name': '\u7279\u6b8a\u88c5\u5907\u6210\u957f\u7387\u5c5e\u6027',
                'verbose_name_plural': '\u7279\u6b8a\u88c5\u5907\u6210\u957f\u7387\u5c5e\u6027',
            },
        ),
        migrations.CreateModel(
            name='EquipmentSpecialLevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('items', models.TextField()),
            ],
            options={
                'db_table': 'equipment_special_level',
                'verbose_name': '\u7279\u6b8a\u88c5\u5907\u7b49\u7ea7',
                'verbose_name_plural': '\u7279\u6b8a\u88c5\u5907\u7b49\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='EquipmentSpecialScoreToGrowing',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tp', models.IntegerField()),
                ('score_low', models.IntegerField()),
                ('score_high', models.IntegerField()),
                ('growing_low', models.IntegerField()),
                ('growing_high', models.IntegerField()),
            ],
            options={
                'db_table': 'equipment_special_score_to_growing',
                'verbose_name': '\u7279\u6b8a\u88c5\u5907\u5206\u6570\u6210\u957f\u7387',
                'verbose_name_plural': '\u7279\u6b8a\u88c5\u5907\u5206\u6570\u6210\u957f\u7387',
            },
        ),
    ]
