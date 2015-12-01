# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0013_auto_20151113_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengetype',
            name='condition_challenge_id',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x89\x8d\xe7\xbd\xae\xe5\x85\xb3\xe5\x8d\xa1ID'),
        ),
    ]
