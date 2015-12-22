# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0010_package_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='baobing',
        ),
        migrations.RemoveField(
            model_name='package',
            name='caozuo',
        ),
        migrations.RemoveField(
            model_name='package',
            name='fangshou',
        ),
        migrations.RemoveField(
            model_name='package',
            name='jingong',
        ),
        migrations.RemoveField(
            model_name='package',
            name='ladder_score',
        ),
        migrations.RemoveField(
            model_name='package',
            name='league_score',
        ),
        migrations.RemoveField(
            model_name='package',
            name='qianzhi',
        ),
        migrations.RemoveField(
            model_name='package',
            name='xintai',
        ),
        migrations.RemoveField(
            model_name='package',
            name='yishi',
        ),
        migrations.RemoveField(
            model_name='package',
            name='yunying',
        ),
        migrations.AddField(
            model_name='package',
            name='lilun',
            field=models.CharField(max_length=32, verbose_name=b'\xe7\x90\x86\xe8\xae\xba', blank=True),
        ),
        migrations.AddField(
            model_name='package',
            name='luoji',
            field=models.CharField(max_length=32, verbose_name=b'\xe9\x80\xbb\xe8\xbe\x91', blank=True),
        ),
        migrations.AddField(
            model_name='package',
            name='meili',
            field=models.CharField(max_length=32, verbose_name=b'\xe9\xad\x85\xe5\x8a\x9b', blank=True),
        ),
        migrations.AddField(
            model_name='package',
            name='minjie',
            field=models.CharField(max_length=32, verbose_name=b'\xe6\x95\x8f\xe6\x8d\xb7', blank=True),
        ),
        migrations.AddField(
            model_name='package',
            name='wuxing',
            field=models.CharField(max_length=32, verbose_name=b'\xe4\xba\x94\xe8\xa1\x8c', blank=True),
        ),
    ]
