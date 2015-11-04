# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_clientconfig_mean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientconfig',
            name='value',
            field=models.TextField(),
        ),
    ]
