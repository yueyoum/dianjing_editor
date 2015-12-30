# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0013_auto_20151225_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='staffs',
            field=models.CharField(help_text=b'id:\xe6\x95\xb0\xe9\x87\x8f,id:\xe6\x95\xb0\xe9\x87\x8f', max_length=255, verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5', blank=True),
        ),
    ]
