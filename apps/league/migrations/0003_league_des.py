# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_auto_20150910_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='des',
            field=models.TextField(verbose_name=b'\xe8\xaf\xb4\xe6\x98\x8e', blank=True),
        ),
    ]
