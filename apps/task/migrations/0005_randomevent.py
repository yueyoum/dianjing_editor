# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_auto_20150910_1735'),
        ('task', '0004_taskstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomEvent',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('icon', models.CharField(max_length=255, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87')),
                ('package', models.ForeignKey(verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1', to='package.Package')),
            ],
            options={
                'db_table': 'random_event',
                'verbose_name': '\u968f\u673a\u4e8b\u4ef6',
                'verbose_name_plural': '\u968f\u673a\u4e8b\u4ef6',
            },
        ),
    ]
