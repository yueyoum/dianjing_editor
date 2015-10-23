# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0010_building_remark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('unlock_type', models.IntegerField(verbose_name=b'\xe8\xa7\xa3\xe9\x94\x81\xe6\x9d\xa1\xe4\xbb\xb6', choices=[(1, b'\xe6\x97\xa0\xe9\x9c\x80\xe8\xa7\xa3\xe9\x94\x81'), (2, b'\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe7\xad\x89\xe7\xba\xa7'), (3, b'VIP\xe7\xad\x89\xe7\xba\xa7')])),
                ('unlock_value', models.IntegerField(default=0, verbose_name=b'\xe8\xa7\xa3\xe9\x94\x81\xe5\x80\xbc')),
                ('income', models.IntegerField(verbose_name=b'\xe6\xaf\x8f\xe5\xa4\xa9\xe8\x8e\xb7\xe5\xbe\x97\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81')),
            ],
            options={
                'db_table': 'shop',
                'verbose_name': '\u7f51\u5e97',
                'verbose_name_plural': '\u7f51\u5e97',
            },
        ),
    ]
