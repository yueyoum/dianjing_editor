# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0009_maps'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengematch',
            name='winning_rates',
            field=models.CommaSeparatedIntegerField(default=b'1,1,1,1,1', max_length=255, verbose_name=b'\xe8\x83\x9c\xe7\x8e\x87\xe5\x88\x97\xe8\xa1\xa8'),
        ),
    ]
