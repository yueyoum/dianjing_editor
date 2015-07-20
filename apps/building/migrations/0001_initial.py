# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'db_table': 'building',
                'verbose_name': '\u8bbe\u65bd',
                'verbose_name_plural': '\u8bbe\u65bd',
            },
        ),
        migrations.CreateModel(
            name='BuildingLevels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(verbose_name=b'\xe7\xad\x89\xe7\xba\xa7', db_index=True)),
                ('up_need_club_level', models.IntegerField(verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe7\xad\x89\xe7\xba\xa7')),
                ('up_need_gold', models.IntegerField(verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81')),
                ('value1', models.IntegerField(null=True, verbose_name=b'\xe5\x80\xbc1', blank=True)),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('building', models.ForeignKey(related_name='levels_info', to='building.Building')),
            ],
            options={
                'db_table': 'building_levels',
            },
        ),
    ]
