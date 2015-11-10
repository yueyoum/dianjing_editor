# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20151110_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='trigger_tp',
            new_name='trigger',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='trigger_rate',
            new_name='trigger_value',
        ),
    ]
