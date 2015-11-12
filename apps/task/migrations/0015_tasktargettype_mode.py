# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0014_auto_20151111_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktargettype',
            name='mode',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\x88\xa4\xe6\x96\xad\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe6\x95\xb0\xe5\x80\xbc\xe7\xb4\xaf\xe5\x8a\xa0'), (2, b'\xe7\x9b\xb4\xe6\x8e\xa5\xe6\xaf\x94\xe8\xbe\x83')]),
        ),
    ]
