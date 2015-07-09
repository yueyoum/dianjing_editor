# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20150709_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffrecruitsettings',
            name='ids',
        ),
        migrations.AddField(
            model_name='staff',
            name='buy_type',
            field=models.IntegerField(default=1, verbose_name=b'\xe7\xad\xbe\xe7\xba\xa6\xe8\xb4\xb9\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'RMB'), (2, b'\xe9\x92\xbb\xe7\x9f\xb3')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='can_recruit',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe4\xbb\xa5\xe6\x8b\x9b\xe5\x8b\x9f'),
        ),
    ]
