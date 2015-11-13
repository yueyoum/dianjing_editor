# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0011_challengetype_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challengematch',
            name='next_id',
        ),
    ]
