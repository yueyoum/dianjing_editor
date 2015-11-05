# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0009_auto_20151103_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillWashCost',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe9\x94\x81\xe5\xae\x9a\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\xb0\xe9\x87\x8f', primary_key=True)),
                ('cost_type', models.IntegerField(verbose_name=b'\xe8\x8a\xb1\xe8\xb4\xb9\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81'), (2, b'\xe9\x92\xbb\xe7\x9f\xb3')])),
                ('cost_value', models.IntegerField(verbose_name=b'\xe8\x8a\xb1\xe8\xb4\xb9\xe9\x87\x91\xe9\xa2\x9d')),
            ],
            options={
                'db_table': 'skill_wash_cost',
                'verbose_name': '\u6280\u80fd\u6d17\u7ec3\u82b1\u8d39',
                'verbose_name_plural': '\u6280\u80fd\u6d17\u7ec3\u82b1\u8d39',
            },
        ),
    ]
