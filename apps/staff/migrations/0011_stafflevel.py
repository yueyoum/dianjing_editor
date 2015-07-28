# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_staff_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffLevel',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe7\xad\x89\xe7\xba\xa7', primary_key=True)),
                ('quality_A', models.IntegerField(verbose_name=b'\xe5\x93\x81\xe8\xb4\xa8A\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe7\xbb\x8f\xe9\xaa\x8c')),
                ('quality_B', models.IntegerField(verbose_name=b'\xe5\x93\x81\xe8\xb4\xa8B\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe7\xbb\x8f\xe9\xaa\x8c')),
                ('quality_C', models.IntegerField(verbose_name=b'\xe5\x93\x81\xe8\xb4\xa8C\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe7\xbb\x8f\xe9\xaa\x8c')),
                ('quality_D', models.IntegerField(verbose_name=b'\xe5\x93\x81\xe8\xb4\xa8D\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe7\xbb\x8f\xe9\xaa\x8c')),
                ('quality_S', models.IntegerField(verbose_name=b'\xe5\x93\x81\xe8\xb4\xa8S\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe7\xbb\x8f\xe9\xaa\x8c')),
                ('quality_SS', models.IntegerField(verbose_name=b'\xe5\x93\x81\xe8\xb4\xa8SS\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe7\xbb\x8f\xe9\xaa\x8c')),
            ],
            options={
                'db_table': 'staff_level',
                'verbose_name': '\u7b49\u7ea7',
                'verbose_name_plural': '\u7b49\u7ea7',
            },
        ),
    ]
