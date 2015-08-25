# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0003_auto_20150713_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='icon',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87'),
            preserve_default=False,
        ),
    ]
