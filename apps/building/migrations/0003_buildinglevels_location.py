# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0002_auto_20150720_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinglevels',
            name='location',
            field=models.CharField(max_length=255, verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae', blank=True),
        ),
    ]
