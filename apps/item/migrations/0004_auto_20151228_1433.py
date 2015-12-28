# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_order_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tp',
            field=models.IntegerField(default=1, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe9\x81\x93\xe5\x85\xb7'), (2, b'\xe7\xbd\x91\xe5\xba\x97\xe8\xb4\xa7\xe7\x89\xa9')]),
        ),
        migrations.AddField(
            model_name='item',
            name='value',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x80\xbc'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sell_gold',
            field=models.IntegerField(default=0, help_text=b'0 \xe8\xa1\xa8\xe7\xa4\xba\xe4\xb8\x8d\xe5\x8f\xaf\xe5\x94\xae\xe5\x8d\x96', verbose_name=b'\xe5\x94\xae\xe5\x8d\x96\xe6\x89\x80\xe5\xbe\x97\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81'),
        ),
    ]
