# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0003_auto_20150713_1639'),
        ('match', '0002_challengematch_next_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengematch',
            name='policy',
            field=models.ForeignKey(default=1, verbose_name=b'\xe6\x88\x98\xe6\x9c\xaf', to='unit.Policy'),
            preserve_default=False,
        ),
    ]
