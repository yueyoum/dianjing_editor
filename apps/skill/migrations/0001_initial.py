# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('addition_ids', models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe5\x8a\xa0\xe6\x88\x90ID\xe5\x88\x97\xe8\xa1\xa8')),
                ('value_base', models.IntegerField(verbose_name=b'\xe5\x9f\xba\xe7\xa1\x80\xe5\x80\xbc')),
                ('level_grow', models.IntegerField(verbose_name=b'\xe7\xad\x89\xe7\xba\xa7\xe5\xa2\x9e\xe9\x95\xbf')),
                ('max_level', models.IntegerField(verbose_name=b'\xe6\x9c\x80\xe5\xa4\xa7\xe7\xad\x89\xe7\xba\xa7')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'skill',
                'verbose_name': '\u6280\u80fd',
                'verbose_name_plural': '\u6280\u80fd',
            },
        ),
        migrations.CreateModel(
            name='SkillAddition',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('add_property', models.CharField(max_length=32, verbose_name=b'\xe5\xa2\x9e\xe5\x8a\xa0\xe5\xb1\x9e\xe6\x80\xa7')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'skill_addition',
                'verbose_name': '\u6280\u80fd\u52a0\u6210',
                'verbose_name_plural': '\u6280\u80fd\u52a0\u6210',
            },
        ),
        migrations.CreateModel(
            name='SkillType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'skill_type',
                'verbose_name': '\u6280\u80fd\u7c7b\u578b',
                'verbose_name_plural': '\u6280\u80fd\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='type_id',
            field=models.ForeignKey(db_column=b'type_id', verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', to='skill.SkillType'),
        ),
    ]
