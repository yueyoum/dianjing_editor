# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0003_auto_20150902_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='arrow',
            field=models.IntegerField(default=1, verbose_name=b'\xe7\xae\xad\xe5\xa4\xb4\xe6\x96\xb9\xe5\x90\x91', choices=[(1, b'\xe4\xb8\x8a'), (2, b'\xe4\xb8\x8b'), (3, b'\xe5\xb7\xa6'), (4, b'\xe5\x8f\xb3')]),
            preserve_default=False,
        ),
    ]
