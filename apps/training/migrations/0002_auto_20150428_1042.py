# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='des',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='icon',
            field=models.CharField(default='', max_length=32, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87'),
            preserve_default=False,
        ),
    ]
