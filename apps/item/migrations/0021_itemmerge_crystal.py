# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-07 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0020_auto_20160307_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmerge',
            name='crystal',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x88\x86\xe8\xa7\xa3\xe8\x8e\xb7\xe5\xbe\x97\xe6\xb0\xb4\xe6\x99\xb6'),
            preserve_default=False,
        ),
    ]