# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0007_buildinglevels_up_need_time_min'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildinglevels',
            name='up_need_time_min',
        ),
        migrations.AddField(
            model_name='buildinglevels',
            name='up_need_minutes',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe5\x88\x86\xe9\x92\x9f\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='buildinglevels',
            name='value2',
            field=models.IntegerField(null=True, verbose_name=b'\xe5\x80\xbc2', blank=True),
        ),
    ]
