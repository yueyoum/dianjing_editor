# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_auto_20151013_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysignin',
            name='mail_content',
            field=models.TextField(verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='activitysignin',
            name='mail_title',
            field=models.CharField(max_length=255, verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe6\xa0\x87\xe9\xa2\x98', blank=True),
        ),
    ]
