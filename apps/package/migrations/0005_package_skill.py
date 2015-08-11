# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_package_trainings'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='skill',
            field=models.CharField(help_text=b'id:level', max_length=255, verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd\xe7\xad\x89\xe7\xba\xa7\xe5\x8a\xa0\xe6\x88\x90', blank=True),
        ),
    ]
