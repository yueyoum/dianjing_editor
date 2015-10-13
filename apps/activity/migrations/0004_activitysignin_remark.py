# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_auto_20151013_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysignin',
            name='remark',
            field=models.TextField(verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
    ]
