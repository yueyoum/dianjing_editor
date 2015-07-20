# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_auto_20150710_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffrecruit',
            name='cost_type',
            field=models.IntegerField(verbose_name=b'\xe8\x8a\xb1\xe8\xb4\xb9\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81'), (2, b'\xe9\x92\xbb\xe7\x9f\xb3')]),
        ),
    ]
