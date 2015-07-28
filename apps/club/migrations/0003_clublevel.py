# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20150716_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubLevel',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe7\xad\x89\xe7\xba\xa7', primary_key=True)),
                ('renown', models.IntegerField(verbose_name=b'\xe5\x8d\x87\xe5\x88\xb0\xe4\xb8\x8b\xe4\xb8\x80\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe5\xa3\xb0\xe6\x9c\x9b')),
            ],
            options={
                'db_table': 'club_level',
                'verbose_name': '\u4ff1\u4e50\u90e8\u7b49\u7ea7',
                'verbose_name_plural': '\u4ff1\u4e50\u90e8\u7b49\u7ea7',
            },
        ),
    ]
