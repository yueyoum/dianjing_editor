# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('errormsg', '0002_errormsg_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errormsg',
            name='des',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
    ]
