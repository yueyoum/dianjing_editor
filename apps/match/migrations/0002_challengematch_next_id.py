# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengematch',
            name='next_id',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xb8\x8b\xe4\xb8\x80\xe5\x85\xb3ID'),
            preserve_default=False,
        ),
    ]
