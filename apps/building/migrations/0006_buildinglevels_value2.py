# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0005_auto_20150917_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinglevels',
            name='value2',
            field=models.IntegerField(null=True, verbose_name=b'\xe5\x80\xbc1', blank=True),
        ),
    ]
