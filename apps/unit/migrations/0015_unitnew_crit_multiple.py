# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-24 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0014_unitnew'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitnew',
            name='crit_multiple',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=8, verbose_name=b'\xe6\x9a\xb4\xe5\x87\xbb\xe8\xa2\xab\xe7\x8e\x87'),
            preserve_default=False,
        ),
    ]
