# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_auto_20150720_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1id', primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\x90\x8d')),
                ('level', models.IntegerField(verbose_name=b'\xe7\xad\x89\xe7\xba\xa7')),
                ('des', models.TextField(verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('num', models.IntegerField(verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe6\xac\xa1\xe6\x95\xb0')),
                ('reward', models.ForeignKey(verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\xa5\x96\xe5\x8a\xb1', to='package.Package')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'task',
                'verbose_name': '\u4efb\u52a1',
                'verbose_name_plural': '\u4efb\u52a1',
            },
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8bid', primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x90\x8d')),
            ],
            options={
                'db_table': 'task_type',
                'verbose_name': '\u4efb\u52a1\u7c7b\u578b',
                'verbose_name_plural': '\u4efb\u52a1\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='tp',
            field=models.ForeignKey(verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe7\xb1\xbb\xe5\x9e\x8b', to='task.TaskType'),
        ),
    ]
