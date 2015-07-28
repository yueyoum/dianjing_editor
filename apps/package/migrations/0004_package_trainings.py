# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_auto_20150720_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='trainings',
            field=models.CharField(help_text=b'id:\xe6\x95\xb0\xe9\x87\x8f,id:\xe6\x95\xb0\xe9\x87\x8f', max_length=255, verbose_name=b'\xe9\x81\x93\xe5\x85\xb7\xef\xbc\x88\xe8\xae\xad\xe7\xbb\x83\xef\xbc\x89', blank=True),
        ),
    ]
