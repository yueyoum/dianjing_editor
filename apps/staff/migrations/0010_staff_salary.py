# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_auto_20150720_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='salary',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\x96\xaa\xe6\xb0\xb4'),
        ),
    ]
