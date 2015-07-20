# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinglevels',
            name='resource',
            field=models.CharField(max_length=255, verbose_name=b'\xe8\xb5\x84\xe6\xba\x90', blank=True),
        ),
        migrations.AlterField(
            model_name='buildinglevels',
            name='des',
            field=models.CharField(max_length=255, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
    ]
