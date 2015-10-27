# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0006_auto_20151019_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'db_table': 'skill_category',
                'verbose_name': '\u5175\u79cd\u7c7b\u522b',
                'verbose_name_plural': '\u5175\u79cd\u7c7b\u522b',
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xe5\x85\xb5\xe7\xa7\x8d\xe7\xb1\xbb\xe5\x88\xab', blank=True, to='skill.SkillCategory', null=True),
        ),
    ]
