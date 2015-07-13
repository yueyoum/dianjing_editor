# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0003_auto_20150521_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='icon',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87'),
            preserve_default=False,
        ),
    ]
