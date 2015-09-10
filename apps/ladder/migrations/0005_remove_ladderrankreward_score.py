# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ladder', '0004_ladderscorestore_des'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ladderrankreward',
            name='score',
        ),
    ]
