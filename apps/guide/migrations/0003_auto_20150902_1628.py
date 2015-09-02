# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_guidedialogafter_guidedialogbefore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='resume_url',
            field=models.CharField(max_length=255, verbose_name=b'\xe6\x81\xa2\xe5\xa4\x8d\xe6\x93\x8d\xe4\xbd\x9c\xe6\xad\xa5\xe9\xaa\xa4', blank=True),
        ),
    ]
