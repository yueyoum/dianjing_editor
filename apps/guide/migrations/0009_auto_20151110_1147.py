# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0008_auto_20151104_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='position',
        ),
        migrations.AddField(
            model_name='guidedialogafter',
            name='icon',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe5\xb0\x8f\xe7\xa7\x98\xe4\xb9\xa6\xe5\x9b\xbe\xe7\x89\x87'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guidedialogafter',
            name='position',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\xb0\x8f\xe7\xa7\x98\xe4\xb9\xa6\xe4\xbd\x8d\xe7\xbd\xae', choices=[(1, b'\xe5\xb7\xa6'), (2, b'\xe5\x8f\xb3')]),
        ),
        migrations.AddField(
            model_name='guidedialogbefore',
            name='icon',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe5\xb0\x8f\xe7\xa7\x98\xe4\xb9\xa6\xe5\x9b\xbe\xe7\x89\x87'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guidedialogbefore',
            name='position',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\xb0\x8f\xe7\xa7\x98\xe4\xb9\xa6\xe4\xbd\x8d\xe7\xbd\xae', choices=[(1, b'\xe5\xb7\xa6'), (2, b'\xe5\x8f\xb3')]),
        ),
    ]
