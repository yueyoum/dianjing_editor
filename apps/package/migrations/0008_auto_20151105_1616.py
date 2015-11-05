# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_auto_20150910_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='trainings',
            field=models.CharField(help_text=b'id:\xe6\x95\xb0\xe9\x87\x8f,id:\xe6\x95\xb0\xe9\x87\x8f', max_length=255, verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd\xe8\xae\xad\xe7\xbb\x83\xe4\xb9\xa6', blank=True),
        ),
    ]
