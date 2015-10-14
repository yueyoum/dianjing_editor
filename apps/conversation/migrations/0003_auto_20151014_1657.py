# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0002_auto_20151014_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='condition_value',
            field=models.CharField(max_length=255, verbose_name=b'\xe6\x9d\xa1\xe4\xbb\xb6\xe5\x80\xbc'),
        ),
    ]
