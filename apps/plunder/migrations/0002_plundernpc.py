# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plunder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlunderNPC',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('level_low', models.IntegerField()),
                ('level_high', models.IntegerField()),
                ('way_one', models.CommaSeparatedIntegerField(max_length=255)),
                ('way_two', models.CommaSeparatedIntegerField(max_length=255)),
                ('way_three', models.CommaSeparatedIntegerField(max_length=255)),
            ],
            options={
                'db_table': 'plunder_npc',
                'verbose_name': '\u63a0\u593aNPC',
                'verbose_name_plural': '\u63a0\u593aNPC',
            },
        ),
    ]
