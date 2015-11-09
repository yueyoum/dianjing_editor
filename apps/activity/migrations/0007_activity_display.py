# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_auto_20151014_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='display',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba'),
        ),
    ]
