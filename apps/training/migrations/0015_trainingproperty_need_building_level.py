# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0014_auto_20151019_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingproperty',
            name='need_building_level',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x89\x80\xe9\x9c\x80\xe5\x9f\xb9\xe8\xae\xad\xe4\xb8\xad\xe5\xbf\x83\xe7\xad\x89\xe7\xba\xa7'),
        ),
    ]
