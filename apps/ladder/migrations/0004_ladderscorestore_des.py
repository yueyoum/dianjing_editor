# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ladder', '0003_auto_20150908_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='ladderscorestore',
            name='des',
            field=models.TextField(default='', verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0'),
            preserve_default=False,
        ),
    ]
