# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0024_shop_goods_max_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='sells_per_hour',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xaf\x8f\xe5\xb0\x8f\xe6\x97\xb6\xe5\x8d\x96\xe5\xa4\x9a\xe5\xb0\x91\xe4\xb8\xaa'),
        ),
    ]
