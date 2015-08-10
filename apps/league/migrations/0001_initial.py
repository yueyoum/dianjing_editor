# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_package_trainings'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe7\xad\x89\xe7\xba\xa7', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('day_reward', models.ForeignKey(related_name='league_day_reward', verbose_name=b'\xe6\x97\xa5\xe5\xa5\x96\xe5\x8a\xb1', to='package.Package')),
                ('week_reward', models.ForeignKey(related_name='league_week_reward', verbose_name=b'\xe5\x91\xa8\xe5\xa5\x96\xe5\x8a\xb1', to='package.Package')),
            ],
            options={
                'db_table': 'league',
                'verbose_name': '\u8054\u8d5b',
                'verbose_name_plural': '\u8054\u8d5b',
            },
        ),
    ]
