# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20150721_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='client_task',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xaf\xe5\xae\xa2\xe6\x88\xb7\xe7\xab\xaf\xe4\xbb\xbb\xe5\x8a\xa1'),
        ),
        migrations.AddField(
            model_name='task',
            name='success_rate',
            field=models.IntegerField(default=100, verbose_name=b'\xe6\x88\x90\xe5\x8a\x9f\xe7\x8e\x87'),
        ),
    ]
