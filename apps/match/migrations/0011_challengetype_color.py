# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0010_challengematch_winning_rates'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengetype',
            name='color',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe9\xa2\x9c\xe8\x89\xb2'),
            preserve_default=False,
        ),
    ]
