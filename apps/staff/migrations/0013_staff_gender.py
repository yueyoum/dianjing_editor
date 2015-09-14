# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0012_staffquality_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.CharField(default='', max_length=32, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab'),
            preserve_default=False,
        ),
    ]
