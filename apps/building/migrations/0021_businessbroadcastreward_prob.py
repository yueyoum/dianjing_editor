# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0020_businessbroadcastreward'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessbroadcastreward',
            name='prob',
            field=models.IntegerField(default=100, verbose_name=b'\xe6\xa6\x82\xe7\x8e\x87'),
        ),
    ]
