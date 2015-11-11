# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('active_value', '0006_auto_20151009_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='activefunction',
            name='ui_name',
            field=models.CharField(max_length=255, verbose_name=b'UI\xe5\x90\x8d', blank=True),
        ),
    ]
