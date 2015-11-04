# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0007_guide_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='operate_target',
            field=models.CharField(max_length=255, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\x9b\xae\xe6\xa0\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='guide',
            name='operate_type',
            field=models.IntegerField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(0, b'\xe7\xa9\xba\xe6\x93\x8d\xe4\xbd\x9c'), (1, b'\xe7\x82\xb9\xe5\x87\xbbUI'), (2, b'\xe6\x8b\x96\xe5\x8a\xa8UI'), (3, b'\xe7\x82\xb9\xe5\x87\xbb\xe5\xbb\xba\xe7\xad\x91')]),
        ),
    ]
