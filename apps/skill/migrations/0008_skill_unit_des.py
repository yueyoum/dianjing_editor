# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0007_auto_20151027_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='unit_des',
            field=models.TextField(verbose_name=b'\xe5\x85\xb5\xe7\xa7\x8d\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
    ]
