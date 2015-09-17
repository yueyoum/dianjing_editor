# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorLogTemplate',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('template', models.TextField()),
            ],
            options={
                'db_table': 'sponsor_log_template',
                'verbose_name': '\u8d5e\u52a9\u4fe1\u606f\u6a21\u677f',
                'verbose_name_plural': '\u8d5e\u52a9\u4fe1\u606f\u6a21\u677f',
            },
        ),
    ]
