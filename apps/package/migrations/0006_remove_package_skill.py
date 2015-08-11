# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0005_package_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='skill',
        ),
    ]
