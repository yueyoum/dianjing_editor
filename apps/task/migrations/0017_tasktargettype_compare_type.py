# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0016_auto_20151112_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktargettype',
            name='compare_type',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xaf\x94\xe8\xbe\x83\xe6\x96\xb9\xe5\xbc\x8f', choices=[(0, b'\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83'), (1, b'>='), (2, b'<=')]),
        ),
    ]
