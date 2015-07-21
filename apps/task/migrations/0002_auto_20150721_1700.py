# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktype',
            name='des',
            field=models.TextField(default=None, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='task',
            name='level',
            field=models.IntegerField(verbose_name=b'\xe6\x89\x80\xe9\x9c\x80\xe4\xbb\xbb\xe5\x8a\xa1\xe4\xb8\xad\xe5\xbf\x83\xe7\xad\x89\xe7\xba\xa7'),
        ),
        migrations.AlterField(
            model_name='tasktype',
            name='name',
            field=models.CharField(unique=True, max_length=32, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x90\x8d'),
        ),
    ]
