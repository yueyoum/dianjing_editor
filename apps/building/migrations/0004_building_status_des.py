# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0003_buildinglevels_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='status_des',
            field=models.TextField(verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
    ]
