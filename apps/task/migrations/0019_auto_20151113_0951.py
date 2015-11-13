# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def change_compare_type_to_1(apps, schema_editor):
    TaskTargetType = apps.get_module("task", "TaskTargetType")
    TaskTargetType.objects.filter(compare_type=0).update(compare_type=1)

class Migration(migrations.Migration):

    dependencies = [
        ('task', '0018_auto_20151113_0949'),
    ]

    operations = [
        migrations.RunPython(change_compare_type_to_1)
    ]
