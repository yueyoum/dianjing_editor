# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0013_auto_20151019_1051'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='trainingskill',
            table='training_skill_item',
        ),
    ]
