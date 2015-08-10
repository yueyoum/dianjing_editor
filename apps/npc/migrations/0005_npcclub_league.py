# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
        ('npc', '0004_auto_20150810_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='npcclub',
            name='league',
            field=models.ForeignKey(default=1, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe8\x81\x94\xe8\xb5\x9b\xe7\xad\x89\xe7\xba\xa7', to='league.League'),
            preserve_default=False,
        ),
    ]
