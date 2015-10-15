# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0005_skill_race'),
        ('package', '0007_auto_20150910_1735'),
        ('training', '0009_auto_20150811_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingProperty',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('icon', models.CharField(max_length=32, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87')),
                ('des', models.TextField(blank=True)),
                ('minutes', models.IntegerField(verbose_name=b'\xe8\xae\xad\xe7\xbb\x83\xe6\x89\x80\xe9\x9c\x80\xe5\x88\x86\xe9\x92\x9f')),
                ('cost_type', models.IntegerField(default=1, verbose_name=b'\xe8\x8a\xb1\xe8\xb4\xb9\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81'), (2, b'\xe9\x92\xbb\xe7\x9f\xb3')])),
                ('cost_value', models.IntegerField(verbose_name=b'\xe8\x8a\xb1\xe8\xb4\xb9\xe9\x87\x91\xe9\xa2\x9d')),
                ('order_value', models.IntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f\xe5\x80\xbc')),
                ('package', models.ForeignKey(verbose_name=b'\xe7\x89\xa9\xe5\x93\x81\xe5\x8c\x85', to='package.Package')),
            ],
            options={
                'db_table': 'training_property',
                'verbose_name': '\u5c5e\u6027\u8bad\u7ec3',
                'verbose_name_plural': '\u5c5e\u6027\u8bad\u7ec3',
            },
        ),
        migrations.CreateModel(
            name='TrainingSkill',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('icon', models.CharField(max_length=32, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87')),
                ('des', models.TextField(blank=True)),
                ('minutes', models.IntegerField(verbose_name=b'\xe8\xae\xad\xe7\xbb\x83\xe6\x89\x80\xe9\x9c\x80\xe5\x88\x86\xe9\x92\x9f')),
                ('skill_level', models.IntegerField(verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xad\x89\xe7\xba\xa7')),
                ('skill_id', models.ForeignKey(verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd', to='skill.Skill')),
            ],
            options={
                'db_table': 'training_skill',
                'verbose_name': '\u6280\u80fd\u8bad\u7ec3',
                'verbose_name_plural': '\u6280\u80fd\u8bad\u7ec3',
            },
        ),
    ]
