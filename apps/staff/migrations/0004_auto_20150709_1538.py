# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20150709_1528'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='staffrecruitsettings',
            unique_together=set([('recruit', 'quality')]),
        ),
    ]
