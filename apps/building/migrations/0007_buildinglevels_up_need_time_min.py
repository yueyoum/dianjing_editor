# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0006_buildinglevels_value2'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinglevels',
            name='up_need_time_min',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
