# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_auto_20151110_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_begin',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\xa4\xb4\xe4\xbb\xbb\xe5\x8a\xa1'),
        ),
    ]
