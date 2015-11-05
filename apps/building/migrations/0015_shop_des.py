# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0014_auto_20151104_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='des',
            field=models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
    ]
