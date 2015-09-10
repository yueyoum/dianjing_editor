# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0006_remove_package_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='ladder_score',
            field=models.CharField(max_length=32, verbose_name=b'\xe5\xa4\xa9\xe6\xa2\xaf\xe8\xb5\x9b\xe7\xa7\xaf\xe5\x88\x86', blank=True),
        ),
        migrations.AddField(
            model_name='package',
            name='league_score',
            field=models.CharField(max_length=32, verbose_name=b'\xe8\x81\x94\xe8\xb5\x9b\xe7\xa7\xaf\xe5\x88\x86', blank=True),
        ),
    ]
