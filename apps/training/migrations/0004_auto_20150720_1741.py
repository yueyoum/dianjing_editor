# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
        ('package', '0003_auto_20150720_1713'),
        ('training', '0003_auto_20150429_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='reward_type',
        ),
        migrations.RemoveField(
            model_name='training',
            name='reward_value',
        ),
        migrations.AddField(
            model_name='training',
            name='building',
            field=models.ForeignKey(default=1, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\xbb\xba\xe7\xad\x91', to='building.Building'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='training',
            name='cost_type',
            field=models.IntegerField(default=1, verbose_name=b'\xe8\x8a\xb1\xe8\xb4\xb9\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81'), (2, b'\xe9\x92\xbb\xe7\x9f\xb3')]),
        ),
        migrations.AddField(
            model_name='training',
            name='cost_value',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\x8a\xb1\xe8\xb4\xb9\xe9\x87\x91\xe9\xa2\x9d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='training',
            name='need_building_level',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x89\x80\xe9\x9c\x80\xe5\xbb\xba\xe7\xad\x91\xe7\x89\xa9\xe7\xad\x89\xe7\xba\xa7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='training',
            name='package',
            field=models.ForeignKey(default=1, verbose_name=b'\xe7\x89\xa9\xe5\x93\x81\xe5\x8c\x85', to='package.Package'),
            preserve_default=False,
        ),
    ]
