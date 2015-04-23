# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorMsg',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('error_index', models.CharField(unique=True, max_length=64)),
                ('text_zh', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'error_msg',
                'verbose_name': '\u9519\u8bef\u4ee3\u7801',
                'verbose_name_plural': '\u9519\u8bef\u4ee3\u7801',
            },
        ),
    ]
