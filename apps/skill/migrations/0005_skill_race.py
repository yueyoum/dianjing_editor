# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_auto_20150720_1741'),
        ('skill', '0004_skill_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(default=1, verbose_name=b'\xe7\xa7\x8d\xe6\x97\x8f', to='staff.StaffRace'),
            preserve_default=False,
        ),
    ]
