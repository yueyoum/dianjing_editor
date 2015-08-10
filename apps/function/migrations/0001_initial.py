# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0003_buildinglevels_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('order_in_building', models.IntegerField(default=1, verbose_name=b'\xe5\x9c\xa8\xe7\x95\x8c\xe9\x9d\xa2\xe4\xb8\xad\xe6\x98\xbe\xe7\xa4\xba\xe9\xa1\xba\xe5\xba\x8f')),
                ('need_building_level', models.IntegerField(default=1, verbose_name=b'\xe6\x89\x80\xe9\x9c\x80\xe5\xbb\xba\xe7\xad\x91\xe7\xad\x89\xe7\xba\xa7')),
                ('unlock_des', models.TextField(verbose_name=b'\xe8\xa7\xa3\xe9\x94\x81\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('belong_to_building', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\xbb\xba\xe7\xad\x91', blank=True, to='building.Building', null=True)),
            ],
            options={
                'db_table': 'function',
                'verbose_name': '\u529f\u80fd',
                'verbose_name_plural': '\u529f\u80fd',
            },
        ),
    ]
