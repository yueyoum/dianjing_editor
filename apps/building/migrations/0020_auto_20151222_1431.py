# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0019_buildinglevels_effect_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingEffect',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name=b'\xe6\x95\x88\xe6\x9e\x9cID')),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\xbb\xba\xe7\xad\x91\xe6\x95\x88\xe6\x9e\x9c\xe5\x90\x8d')),
            ],
            options={
                'db_table': 'building_effect',
                'verbose_name': '\u5efa\u7b51\u6548\u679c',
                'verbose_name_plural': '\u5efa\u7b51\u6548\u679c',
            },
        ),
        migrations.CreateModel(
            name='BuildingEffectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tp', models.IntegerField(choices=[(1, b'\xe6\x8b\x9b\xe5\x8b\x9f\xe8\x8a\xb1\xe8\xb4\xb9\xe5\x87\x8f\xe5\xb0\x91'), (2, b'\xe5\x95\x86\xe5\x8a\xa1\xe6\x94\xb6\xe7\x9b\x8a\xe5\xa2\x9e\xe5\x8a\xa0'), (3, b'\xe7\x9b\xb4\xe6\x92\xad\xe4\xbd\x8d\xe7\xbd\xae\xe5\xa2\x9e\xe5\x8a\xa0'), (4, b'\xe7\xbd\x91\xe5\xba\x97\xe6\x95\xb0\xe9\x87\x8f\xe5\xa2\x9e\xe5\x8a\xa0'), (5, b'\xe5\x90\x88\xe7\xba\xa6\xe6\x95\xb0\xe9\x87\x8f\xe5\xa2\x9e\xe5\x8a\xa0'), (6, b'\xe8\x81\x94\xe8\xb5\x9b\xe7\xbb\x8f\xe9\xaa\x8c\xe5\xa2\x9e\xe5\x8a\xa0'), (7, b'\xe5\x8a\x9f\xe8\x83\xbd\xe5\xbc\x80\xe6\x94\xbe'), (8, b'\xe8\xae\xad\xe7\xbb\x83\xe4\xbd\x8d\xe7\xbd\xae\xe5\xa2\x9e\xe5\x8a\xa0'), (9, b'\xe8\xae\xad\xe7\xbb\x83\xe6\x95\x88\xe6\x9e\x9c\xe5\x8a\xa0\xe6\x88\x90')], verbose_name=b'\xe6\x95\x88\xe6\x9e\x9c\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('value', models.CharField(max_length=255, verbose_name=b'\xe6\x95\x88\xe6\x9e\x9c\xe5\x80\xbc')),
                ('building_effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='effect_id', to='building.BuildingEffect')),
            ],
            options={
                'db_table': 'building_effect_info',
                'verbose_name': '\u5efa\u7b51\u6548\u679c',
                'verbose_name_plural': '\u5efa\u7b51\u6548\u679c',
            },
        ),
        migrations.RemoveField(
            model_name='buildinglevels',
            name='value1',
        ),
        migrations.RemoveField(
            model_name='buildinglevels',
            name='value2',
        ),
        migrations.AddField(
            model_name='buildinglevels',
            name='effect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='building.BuildingEffect', verbose_name=b'\xe5\xbb\xba\xe7\xad\x91\xe6\x95\x88\xe6\x9e\x9c'),
        ),
    ]
