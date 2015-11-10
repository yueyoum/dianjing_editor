# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_auto_20151110_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktargettype',
            name='des',
            field=models.TextField(default='string', verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe7\xb1\xbb\xe5\x9e\x8b\xe6\x8f\x8f\xe8\xbf\xb0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='des',
            field=models.TextField(verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='tasktype',
            name='des',
            field=models.TextField(verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
    ]
