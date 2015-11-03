# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0013_staff_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffquality',
            name='background',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
