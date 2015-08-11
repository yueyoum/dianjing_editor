# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0007_auto_20150810_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='building',
        ),
        migrations.RemoveField(
            model_name='training',
            name='skill_id',
        ),
        migrations.RemoveField(
            model_name='training',
            name='skill_level',
        ),
        migrations.AddField(
            model_name='training',
            name='on_sell',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x87\xba\xe5\x94\xae'),
        ),
        migrations.AlterField(
            model_name='training',
            name='package',
            field=models.ForeignKey(verbose_name=b'\xe7\x89\xa9\xe5\x93\x81\xe5\x8c\x85', to='package.Package'),
        ),
    ]
