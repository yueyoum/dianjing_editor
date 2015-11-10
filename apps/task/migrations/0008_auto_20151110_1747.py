# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20151106_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskTarget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(default=1, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x80\xbc')),
            ],
            options={
                'db_table': 'task_target',
                'verbose_name': '\u4efb\u52a1\u76ee\u6807',
                'verbose_name_plural': '\u4efb\u52a1\u76ee\u6807',
            },
        ),
        migrations.CreateModel(
            name='TaskTargetType',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe7\xb1\xbb\xe5\x9e\x8bid', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x90\x8d')),
            ],
            options={
                'db_table': 'target_type',
                'verbose_name': '\u76ee\u6807\u7c7b\u578b',
                'verbose_name_plural': '\u76ee\u6807\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='TaskTrigger',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe8\xa7\xa6\xe5\x8f\x91\xe7\xb1\xbb\xe5\x9e\x8bid', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name=b'\xe8\xa7\xa6\xe5\x8f\x91\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x90\x8d')),
            ],
            options={
                'db_table': 'task_trigger',
                'verbose_name': '\u4efb\u52a1\u89e6\u53d1',
                'verbose_name_plural': '\u4efb\u52a1\u89e6\u53d1',
            },
        ),
        migrations.RemoveField(
            model_name='task',
            name='des',
        ),
        migrations.RemoveField(
            model_name='task',
            name='level',
        ),
        migrations.RemoveField(
            model_name='task',
            name='num',
        ),
        migrations.RemoveField(
            model_name='taskstatus',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='tasktype',
            name='des',
        ),
        migrations.AddField(
            model_name='task',
            name='next_task',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xb8\x8b\xe4\xb8\x80\xe4\xb8\xaa\xe4\xbb\xbb\xe5\x8a\xa1id'),
        ),
        migrations.AddField(
            model_name='task',
            name='trigger_rate',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xa7\xa6\xe5\x8f\x91\xe5\x80\xbc'),
        ),
        migrations.AddField(
            model_name='tasktarget',
            name='task',
            field=models.ForeignKey(verbose_name=b'task_target', to='task.Task'),
        ),
        migrations.AddField(
            model_name='tasktarget',
            name='tp',
            field=models.ForeignKey(verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe7\xb1\xbb\xe5\x9e\x8b', to='task.TaskTargetType'),
        ),
        migrations.AddField(
            model_name='task',
            name='trigger_tp',
            field=models.ForeignKey(verbose_name=b'\xe8\xa7\xa6\xe5\x8f\x91\xe7\xb1\xbb\xe5\x9e\x8b', blank=True, to='task.TaskTrigger', null=True),
        ),
    ]
