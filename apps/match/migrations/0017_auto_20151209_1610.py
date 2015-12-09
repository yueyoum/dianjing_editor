# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0016_elitearea_elitematch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elitearea',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
        ),
    ]
