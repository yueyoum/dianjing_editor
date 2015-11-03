# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0014_staffquality_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffrace',
            name='icon',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
