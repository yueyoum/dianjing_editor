# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='addition_ids',
            field=models.CommaSeparatedIntegerField(help_text=b'id:value,id:value', max_length=255, verbose_name=b'\xe5\x8a\xa0\xe6\x88\x90ID\xe5\x88\x97\xe8\xa1\xa8'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='level_grow',
            field=models.IntegerField(help_text=b'\xe7\x99\xbe\xe5\x88\x86\xe6\xaf\x94\xe6\x95\xb0\xe5\x80\xbc', verbose_name=b'\xe7\xad\x89\xe7\xba\xa7\xe5\xa2\x9e\xe9\x95\xbf'),
        ),
    ]
