# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0008_auto_20150818_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('picture', models.CharField(max_length=255, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
            ],
            options={
                'db_table': 'maps',
                'verbose_name': '\u5730\u56fe',
                'verbose_name_plural': '\u5730\u56fe',
            },
        ),
    ]
