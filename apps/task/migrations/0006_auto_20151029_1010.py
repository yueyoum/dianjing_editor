# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_randomevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomEventDialogAfter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dialog', models.TextField()),
            ],
            options={
                'db_table': 'random_event_dialog_after',
                'verbose_name': '\u968f\u673a\u4e8b\u4ef6\u540e\u5bf9\u8bdd',
                'verbose_name_plural': '\u968f\u673a\u4e8b\u4ef6\u540e\u5bf9\u8bdd',
            },
        ),
        migrations.CreateModel(
            name='RandomEventDialogBefore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dialog', models.TextField()),
            ],
            options={
                'db_table': 'random_event_dialog_before',
                'verbose_name': '\u968f\u673a\u4e8b\u4ef6\u524d\u5bf9\u8bdd',
                'verbose_name_plural': '\u968f\u673a\u4e8b\u4ef6\u524d\u5bf9\u8bdd',
            },
        ),
        migrations.AddField(
            model_name='randomevent',
            name='level_max',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x9c\x80\xe9\xab\x98\xe7\xad\x89\xe7\xba\xa7'),
        ),
        migrations.AddField(
            model_name='randomevent',
            name='level_min',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x9c\x80\xe4\xbd\x8e\xe7\xad\x89\xe7\xba\xa7'),
        ),
        migrations.AddField(
            model_name='randomevent',
            name='trig_name',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe8\xa7\xa6\xe5\x8f\x91\xe8\x8a\x82\xe7\x82\xb9'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomeventdialogbefore',
            name='random_event',
            field=models.ForeignKey(related_name='dialog_before', to='task.RandomEvent'),
        ),
        migrations.AddField(
            model_name='randomeventdialogafter',
            name='random_event',
            field=models.ForeignKey(related_name='dialog_after', to='task.RandomEvent'),
        ),
    ]
