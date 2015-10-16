# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0011_trainingproperty_need_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='package',
        ),
        migrations.RemoveField(
            model_name='training',
            name='skill_id',
        ),
        migrations.RemoveField(
            model_name='training',
            name='tp',
        ),
        migrations.DeleteModel(
            name='Training',
        ),
        migrations.DeleteModel(
            name='TrainingType',
        ),
    ]
