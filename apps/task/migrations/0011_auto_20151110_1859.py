# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_auto_20151110_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='des',
            field=models.TextField(default='modify', max_length=255, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tasktype',
            name='des',
            field=models.TextField(default='char to text', max_length=255, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
            preserve_default=False,
        ),
    ]
