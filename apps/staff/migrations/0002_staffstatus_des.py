# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffstatus',
            name='des',
            field=models.CharField(max_length=255, verbose_name=b'\xe8\xaf\xb4\xe6\x98\x8e', blank=True),
        ),
    ]
