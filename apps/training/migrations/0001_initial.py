# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('minutes', models.IntegerField(verbose_name=b'\xe8\xae\xad\xe7\xbb\x83\xe6\x89\x80\xe9\x9c\x80\xe5\x88\x86\xe9\x92\x9f')),
                ('reward_type', models.IntegerField(blank=True, null=True, verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe7\xbb\x8f\xe9\xaa\x8c'), (2, b'\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81'), (10, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe9\x9a\x8f\xe6\x9c\xba'), (11, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe8\xbf\x9b\xe6\x94\xbb'), (12, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe7\x89\xb5\xe5\x88\xb6'), (13, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe5\xbf\x83\xe6\x80\x81'), (14, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe6\x9a\xb4\xe5\x85\xb5'), (15, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe9\x98\xb2\xe5\xae\x88'), (16, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe8\xbf\x90\xe8\x90\xa5'), (17, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe6\x84\x8f\xe8\xaf\x86'), (18, b'\xe5\xb1\x9e\xe6\x80\xa7-\xe6\x93\x8d\xe4\xbd\x9c')])),
                ('reward_value', models.IntegerField(verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1\xe5\x80\xbc')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'training',
                'verbose_name': '\u8bad\u7ec3',
                'verbose_name_plural': '\u8bad\u7ec3',
            },
        ),
        migrations.CreateModel(
            name='TrainingType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'training_type',
                'verbose_name': '\u8bad\u7ec3\u7c7b\u578b',
                'verbose_name_plural': '\u8bad\u7ec3\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='training',
            name='tp',
            field=models.ForeignKey(db_column=b'tp', verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', to='training.TrainingType'),
        ),
    ]
