# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_auto_20150910_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveFunction',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, verbose_name=b'\xe5\x8a\x9f\xe8\x83\xbdID', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x8a\x9f\xe8\x83\xbd\xe5\x90\x8d\xe5\xad\x97')),
                ('value', models.IntegerField(verbose_name=b'\xe6\xaf\x8f\xe6\xac\xa1\xe5\xa5\x96\xe5\x8a\xb1\xe5\xa4\x9a\xe5\xb0\x91\xe6\xb4\xbb\xe8\xb7\x83\xe5\xba\xa6')),
                ('max_times', models.IntegerField(verbose_name=b'\xe6\xaf\x8f\xe5\xa4\xa9\xe6\x9c\x80\xe5\xa4\x9a\xe5\xa5\x96\xe5\x8a\xb1\xe5\xa4\x9a\xe5\xb0\x91\xe6\xac\xa1')),
            ],
            options={
                'db_table': 'active_function',
                'verbose_name': '\u6d3b\u8dc3\u5ea6\u529f\u80fd',
                'verbose_name_plural': '\u6d3b\u8dc3\u5ea6\u529f\u80fd',
            },
        ),
        migrations.CreateModel(
            name='ActiveReward',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe6\xb4\xbb\xe8\xb7\x83\xe5\xba\xa6', primary_key=True)),
                ('package', models.ForeignKey(verbose_name=b'\xe7\x89\xa9\xe5\x93\x81\xe5\x8c\x85', to='package.Package')),
            ],
            options={
                'db_table': 'active_reward',
                'verbose_name': '\u6d3b\u8dc3\u5ea6\u5956\u52b1',
                'verbose_name_plural': '\u6d3b\u8dc3\u5ea6\u5956\u52b1',
            },
        ),
    ]
