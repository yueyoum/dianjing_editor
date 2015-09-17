# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0004_building_status_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinglevels',
            name='up_need_diamond',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe9\x92\xbb\xe7\x9f\xb3'),
        ),
        migrations.AlterField(
            model_name='buildinglevels',
            name='up_need_gold',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81'),
        ),
    ]
