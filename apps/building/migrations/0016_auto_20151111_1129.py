# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0015_shop_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='day_effect',
            field=models.CharField(max_length=255, verbose_name=b'\xe7\x99\xbd\xe5\xa4\xa9\xe6\x95\x88\xe6\x9e\x9c', blank=True),
        ),
        migrations.AddField(
            model_name='building',
            name='night_effect',
            field=models.CharField(max_length=255, verbose_name=b'\xe6\x99\x9a\xe4\xb8\x8a\xe6\x95\x88\xe6\x9e\x9c', blank=True),
        ),
    ]
