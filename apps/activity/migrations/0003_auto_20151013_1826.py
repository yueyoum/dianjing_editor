# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20150921_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitysignin',
            name='circle_times',
        ),
        migrations.RemoveField(
            model_name='activitysignin',
            name='valid_test_divisor',
        ),
        migrations.RemoveField(
            model_name='activitysignin',
            name='valid_test_value',
        ),
        migrations.AlterField(
            model_name='activitysignin',
            name='circle_package',
            field=models.ForeignKey(verbose_name=b'\xe5\xa4\xa7\xe5\xa5\x96', to='package.Package', null=True),
        ),
    ]
