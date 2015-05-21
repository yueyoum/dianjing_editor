# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0002_auto_20150521_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='addition_ids',
            field=models.CharField(help_text=b'id:value,id:value', max_length=255, verbose_name=b'\xe5\x8a\xa0\xe6\x88\x90ID\xe5\x88\x97\xe8\xa1\xa8'),
        ),
    ]
