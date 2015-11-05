# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_auto_20151104_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='clublevel',
            name='max_staff_amount',
            field=models.IntegerField(default=5, verbose_name=b'\xe6\x9c\x80\xe5\xa4\xa7\xe5\x91\x98\xe5\xb7\xa5\xe6\x95\xb0'),
            preserve_default=False,
        ),
    ]
