# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-08 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('function', '0007_auto_20160623_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionTips',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('level', models.IntegerField()),
                ('tp', models.IntegerField()),
                ('target', models.CharField(max_length=255)),
                ('des', models.TextField()),
            ],
            options={
                'db_table': 'function_tips',
                'verbose_name': '\u529f\u80fd\u5f00\u653e\u63d0\u793a',
                'verbose_name_plural': '\u529f\u80fd\u5f00\u653e\u63d0\u793a',
            },
        ),
    ]
