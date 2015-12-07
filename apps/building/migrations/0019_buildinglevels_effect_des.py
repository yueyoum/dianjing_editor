# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0018_buildinglevels_up_need_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinglevels',
            name='effect_des',
            field=models.CharField(max_length=255, verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x95\x88\xe6\x9e\x9c\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
    ]
