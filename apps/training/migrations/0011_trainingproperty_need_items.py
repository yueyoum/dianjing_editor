# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0010_trainingproperty_trainingskill'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingproperty',
            name='need_items',
            field=models.CharField(default='', help_text=b'id:\xe6\x95\xb0\xe9\x87\x8f,id:\xe6\x95\xb0\xe9\x87\x8f', max_length=255, verbose_name=b'\xe6\x89\x80\xe9\x9c\x80\xe7\x89\xa9\xe5\x93\x81'),
            preserve_default=False,
        ),
    ]
