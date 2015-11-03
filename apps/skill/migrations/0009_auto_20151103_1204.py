# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0008_skill_unit_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(verbose_name=b'\xe7\xa7\x8d\xe6\x97\x8f', blank=True, to='staff.StaffRace', null=True),
        ),
    ]
