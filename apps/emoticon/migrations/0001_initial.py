# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emoticon',
            fields=[
                ('cmd', models.CharField(max_length=255, serialize=False, verbose_name=b'\xe5\x91\xbd\xe4\xbb\xa4', primary_key=True)),
                ('icon', models.CharField(max_length=255, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87')),
            ],
            options={
                'db_table': 'emoticon',
                'verbose_name': '\u8868\u60c5',
                'verbose_name_plural': '\u8868\u60c5',
            },
        ),
    ]
