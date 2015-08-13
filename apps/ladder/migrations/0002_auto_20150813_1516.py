# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ladder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ladderrankreward',
            name='package',
            field=models.ForeignKey(verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1\xe7\x89\xa9\xe5\x93\x81\xe5\x8c\x85', blank=True, to='package.Package', null=True),
        ),
        migrations.AlterField(
            model_name='ladderrankreward',
            name='score',
            field=models.IntegerField(verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1\xe7\xa7\xaf\xe5\x88\x86'),
        ),
    ]
