# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_activitysignin_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysignin',
            name='circle_package',
            field=models.ForeignKey(verbose_name=b'\xe5\xa4\xa7\xe5\xa5\x96', blank=True, to='package.Package', null=True),
        ),
    ]
