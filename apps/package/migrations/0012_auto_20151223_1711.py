# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0011_auto_20151222_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='lilun',
        ),
        migrations.RemoveField(
            model_name='package',
            name='luoji',
        ),
        migrations.RemoveField(
            model_name='package',
            name='meili',
        ),
        migrations.RemoveField(
            model_name='package',
            name='minjie',
        ),
        migrations.RemoveField(
            model_name='package',
            name='wuxing',
        ),
        migrations.AddField(
            model_name='package',
            name='baobing',
            field=models.CharField(max_length=32, verbose_name=b'\xe6\x9a\xb4\xe5\x85\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='package',
            name='biaoyan',
            field=models.CharField(max_length=32, verbose_name=b'\xe8\xa1\xa8\xe6\xbc\x94', blank=True),
        ),
        migrations.AddField(
            model_name='package',
            name='caozuo',
            field=models.CharField(max_length=32, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c', blank=True),
        ),
        migrations.AddField(
            model_name='package',
            name='yingxiao',
            field=models.CharField(max_length=32, verbose_name=b'\xe8\x90\xa5\xe9\x94\x80', blank=True),
        ),
        migrations.AddField(
            model_name='package',
            name='yunying',
            field=models.CharField(max_length=32, verbose_name=b'\xe8\xbf\x90\xe8\x90\xa5', blank=True),
        ),
        migrations.AddField(
            model_name='package',
            name='zhanshu',
            field=models.CharField(max_length=32, verbose_name=b'\xe6\x88\x98\xe6\x9c\xaf', blank=True),
        ),
    ]
