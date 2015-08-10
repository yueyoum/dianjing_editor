# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('npc', '0003_auto_20150511_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='npcclub',
            name='skill_high',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd\xe7\xad\x89\xe7\xba\xa7\xe4\xb8\x8a\xe9\x99\x90'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='npcclub',
            name='skill_low',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd\xe7\xad\x89\xe7\xba\xa7\xe4\xb8\x8b\xe9\x99\x90'),
            preserve_default=False,
        ),
    ]
