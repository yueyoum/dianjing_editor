# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe4\xbc\x9a\xe8\xaf\x9did', primary_key=True)),
                ('tp', models.IntegerField(verbose_name=b'\xe8\xa7\xa6\xe5\x8f\x91\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe7\x82\xb9\xe5\x87\xbb\xe5\xbb\xba\xe7\xad\x91'), (2, b'\xe6\x8c\x91\xe6\x88\x98\xe5\x85\xb3\xe5\x8d\xa1'), (3, b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x8c\x89\xe9\x92\xae')])),
                ('condition_value', models.CharField(max_length=64, verbose_name=b'\xe8\xa7\xa6\xe5\x8f\x91\xe6\x9d\xa1\xe4\xbb\xb6')),
                ('is_loop', models.BooleanField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xbe\xaa\xe7\x8e\xaf')),
                ('time_tp', models.IntegerField(verbose_name=b'\xe8\xa7\xa6\xe5\x8f\x91\xe6\x97\xb6\xe9\x97\xb4', choices=[(1, b'\xe6\x88\x98\xe6\x96\x97\xe5\xbc\x80\xe5\xa7\x8b\xe8\xa7\xa6\xe5\x8f\x91'), (2, b'\xe6\x88\x98\xe6\x96\x97\xe7\xbb\x93\xe6\x9d\x9f\xe8\xa7\xa6\xe5\x8f\x91')])),
                ('conversation', models.TextField(verbose_name=b'\xe5\x89\xa7\xe6\x83\x85')),
            ],
            options={
                'db_table': 'trigger',
            },
        ),
    ]
