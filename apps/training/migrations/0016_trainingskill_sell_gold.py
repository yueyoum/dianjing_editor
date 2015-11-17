# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0015_trainingproperty_need_building_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingskill',
            name='sell_gold',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x94\xae\xe5\x8d\x96\xe6\x89\x80\xe5\xbe\x97\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81'),
        ),
    ]
