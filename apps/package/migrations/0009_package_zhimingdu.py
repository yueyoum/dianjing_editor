# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0008_auto_20151105_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='zhimingdu',
            field=models.CharField(max_length=32, verbose_name=b'\xe7\x9f\xa5\xe5\x90\x8d\xe5\xba\xa6', blank=True),
        ),
    ]
