# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20151110_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasktarget',
            old_name='task_id',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='tasktarget',
            old_name='tp_id',
            new_name='tp',
        ),
        migrations.RenameField(
            model_name='tasktarget',
            old_name='tp_num',
            new_name='value',
        ),
    ]
