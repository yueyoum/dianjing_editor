# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20151228_1433'),
        ('building', '0021_businessbroadcastreward_prob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='income',
        ),
        migrations.AddField(
            model_name='shop',
            name='goods',
            field=models.ForeignKey(verbose_name=b'\xe5\x94\xae\xe5\x8d\x96\xe8\xb4\xa7\xe7\x89\xa9', blank=True, to='item.Item', null=True),
        ),
    ]
