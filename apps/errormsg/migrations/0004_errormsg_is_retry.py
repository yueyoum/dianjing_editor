# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('errormsg', '0003_auto_20150423_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='errormsg',
            name='is_retry',
            field=models.BooleanField(default=True),
        ),
    ]
