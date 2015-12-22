# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ladder', '0006_auto_20151112_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ladderrankreward',
            name='package',
        ),
        migrations.AddField(
            model_name='ladderrankreward',
            name='reward_gold',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1\xe8\xbd\xaf\xe5\xa6\xb9\xe5\xb8\x81'),
        ),
        migrations.AddField(
            model_name='ladderrankreward',
            name='reward_score',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1\xe7\xa7\xaf\xe5\x88\x86'),
        ),
    ]
