# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0016_auto_20151111_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildinglevels',
            name='up_need_club_level',
        ),
        migrations.AddField(
            model_name='building',
            name='level_up_condition_type',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe6\x9d\xa1\xe4\xbb\xb6', choices=[(1, b'\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe7\xad\x89\xe7\xba\xa7'), (2, b'\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe6\x80\xbb\xe9\x83\xa8\xe5\xa4\xa7\xe6\xa5\xbc\xe7\xad\x89\xe7\xba\xa7')]),
        ),
        migrations.AddField(
            model_name='buildinglevels',
            name='up_condition_value',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x9d\xa1\xe4\xbb\xb6\xe5\x80\xbc'),
            preserve_default=False,
        ),
    ]
