# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qianban', '0002_auto_20150820_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qianban',
            name='addition_value',
            field=models.CharField(help_text=b'\xe5\xa6\x82\xe6\x9e\x9c\xe5\x8a\xa0\xe6\x88\x90\xe7\xb1\xbb\xe5\x9e\x8b\xe6\x98\xaf \xe6\x8a\x80\xe8\x83\xbd\xe5\xbc\xba\xe5\xba\xa6\xef\xbc\x8c\xe8\xbf\x99\xe9\x87\x8c\xe5\xa1\xab\xe5\x86\x99\xe7\x9a\x84\xe6\x98\xaf \xe6\x8a\x80\xe8\x83\xbdid:\xe5\xbc\xba\xe5\xba\xa6', max_length=255, verbose_name=b'\xe5\x8a\xa0\xe6\x88\x90\xe5\x80\xbc'),
        ),
    ]
