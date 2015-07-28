# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_package_trainings'),
        ('match', '0006_auto_20150716_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengematch',
            name='package',
            field=models.ForeignKey(default=1, verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1\xe7\x89\xa9\xe5\x93\x81\xe5\x8c\x85', to='package.Package'),
            preserve_default=False,
        ),
    ]
