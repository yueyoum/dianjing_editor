# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_clublevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='clublevel',
            name='tibu_slot_amount',
            field=models.IntegerField(default=5, verbose_name=b'\xe6\x9b\xbf\xe8\xa1\xa5\xe6\xa0\xbc\xe5\xad\x90\xe6\x95\xb0'),
        ),
    ]
