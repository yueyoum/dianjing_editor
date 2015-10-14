# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'verbose_name': '\u5267\u60c5', 'verbose_name_plural': '\u5267\u60c5'},
        ),
        migrations.AlterField(
            model_name='conversation',
            name='condition_value',
            field=models.CharField(max_length=64, verbose_name=b'\xe6\x9d\xa1\xe4\xbb\xb6\xe5\x80\xbc'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='tp',
            field=models.IntegerField(verbose_name=b'\xe8\xa7\xa6\xe5\x8f\x91\xe6\x9d\xa1\xe4\xbb\xb6', choices=[(1, b'\xe7\x82\xb9\xe5\x87\xbb\xe5\xbb\xba\xe7\xad\x91'), (2, b'\xe6\x8c\x91\xe6\x88\x98\xe5\x85\xb3\xe5\x8d\xa1'), (3, b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x8c\x89\xe9\x92\xae')]),
        ),
        migrations.AlterModelTable(
            name='conversation',
            table='conversation',
        ),
    ]
