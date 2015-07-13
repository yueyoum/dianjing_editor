# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0002_auto_20150713_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitdes',
            name='policy',
            field=models.ForeignKey(verbose_name=b'\xe6\x88\x98\xe6\x9c\xaf', to='unit.Policy'),
        ),
    ]
