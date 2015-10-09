# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('active_value', '0004_auto_20151009_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='activefunction',
            name='des',
            field=models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
    ]
