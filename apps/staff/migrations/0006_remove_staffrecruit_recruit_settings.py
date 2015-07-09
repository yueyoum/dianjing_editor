# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20150709_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffrecruit',
            name='recruit_settings',
        ),
    ]
