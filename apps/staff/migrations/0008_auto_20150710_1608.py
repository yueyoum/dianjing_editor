# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_auto_20150709_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='qianban_ids',
            field=models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe7\x89\xb5\xe7\xbb\x8aID\xe5\x88\x97\xe8\xa1\xa8', blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='skill_ids',
            field=models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe6\x8a\x80\xe8\x83\xbdID\xe5\x88\x97\xe8\xa1\xa8', blank=True),
        ),
    ]
