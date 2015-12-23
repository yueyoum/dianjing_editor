# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0005_auto_20151223_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='icon',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
