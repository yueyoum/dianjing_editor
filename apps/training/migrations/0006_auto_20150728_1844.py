# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20150728_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='package',
            field=models.ForeignKey(verbose_name=b'\xe7\x89\xa9\xe5\x93\x81\xe5\x8c\x85', blank=True, to='package.Package', null=True),
        ),
    ]
