# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('icon', models.CharField(max_length=255, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('buy_type', models.IntegerField(default=0, verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(0, b'\xe4\xb8\x8d\xe5\x8f\xaf\xe8\xb4\xad\xe4\xb9\xb0'), (1, b'\xe7\x94\xa8 \xe9\x92\xbb\xe7\x9f\xb3 \xe8\xb4\xad\xe4\xb9\xb0'), (2, b'\xe7\x94\xa8 \xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81 \xe8\xb4\xad\xe4\xb9\xb0')])),
                ('buy_cost', models.IntegerField(default=0, verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe8\x8a\xb1\xe8\xb4\xb9')),
                ('sell_gold', models.IntegerField(default=0, verbose_name=b'\xe5\x94\xae\xe5\x8d\x96\xe6\x89\x80\xe5\xbe\x97\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81')),
            ],
            options={
                'db_table': 'item',
                'verbose_name': '\u7269\u54c1',
                'verbose_name_plural': '\u7269\u54c1',
            },
        ),
    ]
