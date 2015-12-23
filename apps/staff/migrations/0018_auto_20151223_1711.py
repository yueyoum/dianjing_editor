# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0017_auto_20151222_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='lilun_grow',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='luoji_grow',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='meili_grow',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='minjie_grow',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='wuxing_grow',
        ),
    ]
