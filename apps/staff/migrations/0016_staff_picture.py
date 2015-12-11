# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0015_staffrace_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='picture',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe5\x8d\x8a\xe8\xba\xab\xe5\x83\x8f'),
            preserve_default=False,
        ),
    ]
