# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qianban', '0003_auto_20150820_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qianban',
            name='addition_tp',
            field=models.CharField(max_length=255, verbose_name=b'\xe5\x8a\xa0\xe6\x88\x90\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'luoji', b'\xe9\x80\xbb\xe8\xbe\x91'), (b'minjie', b'\xe6\x95\x8f\xe6\x8d\xb7'), (b'lilun', b'\xe7\x90\x86\xe8\xae\xba'), (b'wuxing', b'\xe4\xba\x94\xe8\xa1\x8c'), (b'meili', b'\xe9\xad\x85\xe5\x8a\x9b'), (b'skill', b'\xe6\x8a\x80\xe8\x83\xbd\xe5\xbc\xba\xe5\xba\xa6')]),
        ),
    ]
