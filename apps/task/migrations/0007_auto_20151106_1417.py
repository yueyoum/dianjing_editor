# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20151029_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='randomeventdialogafter',
            name='icon',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe5\xaf\xb9\xe8\xaf\x9d\xe8\x80\x85\xe5\x9b\xbe\xe6\xa0\x87'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomeventdialogafter',
            name='position',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\xaf\xb9\xe8\xaf\x9d\xe8\x80\x85\xe4\xbd\x8d\xe7\xbd\xae', choices=[(1, b'\xe5\x9c\xa8\xe5\xb7\xa6\xe8\xbe\xb9'), (2, b'\xe5\x9c\xa8\xe5\x8f\xb3\xe8\xbe\xb9')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomeventdialogbefore',
            name='icon',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe5\xaf\xb9\xe8\xaf\x9d\xe8\x80\x85\xe5\x9b\xbe\xe6\xa0\x87'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randomeventdialogbefore',
            name='position',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\xaf\xb9\xe8\xaf\x9d\xe8\x80\x85\xe4\xbd\x8d\xe7\xbd\xae', choices=[(1, b'\xe5\x9c\xa8\xe5\xb7\xa6\xe8\xbe\xb9'), (2, b'\xe5\x9c\xa8\xe5\x8f\xb3\xe8\xbe\xb9')]),
            preserve_default=False,
        ),
    ]
