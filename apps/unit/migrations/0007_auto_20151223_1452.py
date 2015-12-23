# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0006_unit_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='trig_at',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x87\xba\xe5\x85\xb5\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='unit',
            name='trig_prob',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x87\xba\xe5\x85\xb5\xe5\x87\xa0\xe7\x8e\x87'),
        ),
    ]
