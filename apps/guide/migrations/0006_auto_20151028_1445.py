# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_auto_20150910_1735'),
        ('guide', '0005_auto_20150911_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='package',
            field=models.ForeignKey(verbose_name=b'\xe7\x89\xa9\xe5\x93\x81\xe5\x8c\x85', blank=True, to='package.Package', null=True),
        ),
        migrations.AddField(
            model_name='guide',
            name='position',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\xb0\x8f\xe7\xa7\x98\xe4\xb9\xa6\xe4\xbd\x8d\xe7\xbd\xae', choices=[(1, b'\xe5\xb7\xa6'), (2, b'\xe5\x8f\xb3')]),
        ),
    ]
