# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0013_auto_20151023_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='mail_content',
            field=models.TextField(default='', verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='mail_title',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe6\xa0\x87\xe9\xa2\x98'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsor',
            name='mail_content',
            field=models.TextField(default='', verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsor',
            name='mail_title',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe6\xa0\x87\xe9\xa2\x98'),
            preserve_default=False,
        ),
    ]
