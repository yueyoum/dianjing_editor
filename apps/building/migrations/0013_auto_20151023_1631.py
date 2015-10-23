# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0012_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='condition_des',
            field=models.TextField(verbose_name=b'\xe6\x9d\xa1\xe4\xbb\xb6\xe8\xaf\xb4\xe6\x98\x8e', blank=True),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='income',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xaf\x8f\xe5\xa4\xa9\xe6\x94\xb6\xe5\x85\xa5\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsor',
            name='income_des',
            field=models.TextField(verbose_name=b'\xe6\x94\xb6\xe5\x85\xa5\xe8\xaf\xb4\xe6\x98\x8e', blank=True),
        ),
    ]
