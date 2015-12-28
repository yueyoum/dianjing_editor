# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0023_auto_20151228_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='goods_max_amount',
            field=models.IntegerField(default=1000, verbose_name=b'\xe8\xb4\xa7\xe7\x89\xa9\xe6\x9c\x80\xe5\xa4\xa7\xe6\x95\xb0\xe9\x87\x8f'),
        ),
    ]
