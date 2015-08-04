# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('template', models.TextField()),
            ],
            options={
                'db_table': 'notification',
                'verbose_name': '\u901a\u77e5',
                'verbose_name_plural': '\u901a\u77e5',
            },
        ),
    ]
