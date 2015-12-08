# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0010_package_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingMatchReward',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe7\xac\xac\xe5\x87\xa0\xe5\x9c\xba', primary_key=True)),
                ('des', models.TextField(blank=True)),
                ('additional_reward', models.ForeignKey(related_name='tmrar', verbose_name=b'\xe9\xa2\x9d\xe5\xa4\x96\xe5\xa5\x96\xe5\x8a\xb1', blank=True, to='package.Package', null=True)),
                ('reward', models.ForeignKey(related_name='tmr', verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1', to='package.Package')),
            ],
            options={
                'db_table': 'training_match_reward',
                'verbose_name': '\u8bad\u7ec3\u8d5b\u5956\u52b1',
                'verbose_name_plural': '\u8bad\u7ec3\u8d5b\u5956\u52b1',
            },
        ),
    ]
