# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('next_id', models.IntegerField(default=0, verbose_name=b'\xe4\xb8\x8b\xe4\xb8\x80\xe6\xad\xa5ID')),
                ('operate_type', models.IntegerField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe7\x82\xb9\xe5\x87\xbbUI'), (2, b'\xe6\x8b\x96\xe5\x8a\xa8UI'), (3, b'\xe7\x82\xb9\xe5\x87\xbb\xe5\xbb\xba\xe7\xad\x91')])),
                ('operate_target', models.CharField(max_length=255, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\x9b\xae\xe6\xa0\x87')),
                ('resume_url', models.CharField(max_length=255, verbose_name=b'\xe6\x81\xa2\xe5\xa4\x8d\xe6\x93\x8d\xe4\xbd\x9c\xe6\xad\xa5\xe9\xaa\xa4')),
            ],
            options={
                'db_table': 'guide',
                'verbose_name': '\u65b0\u624b\u5f15\u5bfc',
                'verbose_name_plural': '\u65b0\u624b\u5f15\u5bfc',
            },
        ),
    ]
