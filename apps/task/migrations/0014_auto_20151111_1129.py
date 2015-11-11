# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0013_task_task_begin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_begin',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xaf\xe4\xbb\xbb\xe5\x8a\xa1\xe9\x93\xbe\xe5\xa4\xb4'),
        ),
    ]
