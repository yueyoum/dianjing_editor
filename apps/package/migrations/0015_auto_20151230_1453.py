# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0014_package_staffs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='staffs',
            field=models.CommaSeparatedIntegerField(help_text=b'id,id,id', max_length=255, verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5', blank=True),
        ),
    ]
