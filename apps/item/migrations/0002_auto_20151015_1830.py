# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='buy_type',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(0, b'\xe4\xb8\x8d\xe5\x8f\xaf\xe8\xb4\xad\xe4\xb9\xb0'), (1, b'\xe7\x94\xa8 \xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81 \xe8\xb4\xad\xe4\xb9\xb0'), (2, b'\xe7\x94\xa8 \xe9\x92\xbb\xe7\x9f\xb3 \xe8\xb4\xad\xe4\xb9\xb0')]),
        ),
    ]
