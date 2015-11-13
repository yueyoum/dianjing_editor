# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0019_auto_20151113_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='randomevent',
            name='target',
        ),
        migrations.RemoveField(
            model_name='tasktargettype',
            name='type_category',
        ),
        migrations.AddField(
            model_name='tasktarget',
            name='param',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe5\x8f\x82\xe6\x95\xb0'),
        ),
        migrations.AddField(
            model_name='tasktargettype',
            name='has_param',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe7\x9b\xae\xe6\xa0\x87\xe5\x8f\x82\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='tasktarget',
            name='value',
            field=models.IntegerField(default=1, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe5\x80\xbc'),
        ),
    ]
