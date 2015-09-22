# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20150922_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'task_status',
                'verbose_name': '\u4efb\u52a1\u72b6\u6001',
                'verbose_name_plural': '\u4efb\u52a1\u72b6\u6001',
            },
        ),
    ]
