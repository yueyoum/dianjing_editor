# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'resource',
                'verbose_name': '\u8d44\u6e90',
                'verbose_name_plural': '\u8d44\u6e90',
            },
        ),
    ]
