# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20151015_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='order_value',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f\xe5\x80\xbc'),
        ),
    ]
