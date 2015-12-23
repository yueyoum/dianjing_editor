# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qianban', '0005_auto_20151223_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qianban',
            name='addition_tp',
            field=models.CharField(max_length=255, verbose_name=b'\xe5\x8a\xa0\xe6\x88\x90\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'caozuo', b'\xe6\x93\x8d\xe4\xbd\x9c'), (b'baobing', b'\xe6\x9a\xb4\xe5\x85\xb5'), (b'yunying', b'\xe8\xbf\x90\xe8\x90\xa5'), (b'zhanshu', b'\xe6\x88\x98\xe6\x9c\xaf'), (b'biaoyan', b'\xe8\xa1\xa8\xe6\xbc\x94'), (b'biaoyan', b'\xe8\x90\xa5\xe9\x94\x80'), (b'skill', b'\xe6\x8a\x80\xe8\x83\xbd\xe5\xbc\xba\xe5\xba\xa6')]),
        ),
    ]
