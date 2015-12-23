# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('npc', '0006_auto_20151223_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='npcclub',
            name='yunying',
        ),
        migrations.AddField(
            model_name='npcclub',
            name='jingying',
            field=models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe7\xbb\x8f\xe8\x90\xa5\xe8\x8c\x83\xe5\x9b\xb4', blank=True),
        ),
    ]
