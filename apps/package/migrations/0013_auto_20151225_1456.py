# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0012_auto_20151223_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='yunying',
        ),
        migrations.AddField(
            model_name='package',
            name='jingying',
            field=models.CharField(max_length=32, verbose_name=b'\xe7\xbb\x8f\xe8\x90\xa5', blank=True),
        ),
    ]
