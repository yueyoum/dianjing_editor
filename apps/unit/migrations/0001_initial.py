# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0001_initial'),
        ('staff', '0002_staffstatus_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x85\xb5\xe7\xa7\x8d')),
                ('first_trig', models.IntegerField(verbose_name=b'\xe5\xbc\x80\xe5\xb1\x80\xe8\xa7\xa6\xe5\x8f\x91\xe5\x80\xbc')),
                ('second_trig', models.IntegerField(verbose_name=b'\xe4\xb8\xad\xe9\x97\xb4\xe5\xb1\x80\xe8\xa7\xa6\xe5\x8f\x91\xe5\x80\xbc')),
                ('third_trig', models.IntegerField(verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe5\xb1\x80\xe8\xa7\xa6\xe5\x8f\x91\xe5\x80\xbc')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('race', models.ForeignKey(verbose_name=b'\xe7\xa7\x8d\xe6\x97\x8f', to='staff.StaffRace')),
                ('skill', models.ForeignKey(verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd', to='skill.Skill')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'unit',
                'verbose_name': '\u5355\u4f4d',
                'verbose_name_plural': '\u5355\u4f4d',
            },
        ),
    ]
