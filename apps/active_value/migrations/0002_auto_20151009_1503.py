# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('active_value', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activefunction',
            name='name',
        ),
        migrations.AddField(
            model_name='activefunction',
            name='function_sign',
            field=models.CharField(default='x', max_length=255, verbose_name=b'\xe5\x8a\x9f\xe8\x83\xbd\xe6\xa0\x87\xe8\xaf\x86'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activefunction',
            name='id',
            field=models.CharField(max_length=255, serialize=False, verbose_name=b'\xe5\x8a\x9f\xe8\x83\xbd\xe5\x90\x8d\xe5\xad\x97', primary_key=True),
        ),
    ]
