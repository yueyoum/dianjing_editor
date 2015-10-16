# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0008_auto_20151015_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildinglevels',
            name='up_need_diamond',
        ),
    ]
