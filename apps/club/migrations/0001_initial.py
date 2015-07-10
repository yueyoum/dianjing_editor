# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClubFlag',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('flag', models.CharField(max_length=255, verbose_name=b'\xe6\x97\x97\xe5\xb8\x9c')),
            ],
            options={
                'db_table': 'club_flag',
                'verbose_name': '\u4ff1\u4e50\u90e8\u56fe\u6807',
                'verbose_name_plural': '\u4ff1\u4e50\u90e8\u56fe\u6807',
            },
        ),
    ]
