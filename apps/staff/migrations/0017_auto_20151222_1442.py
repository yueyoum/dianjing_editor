# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0016_staff_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='baobing',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='baobing_grow',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='caozuo',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='caozuo_grow',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='fangshou',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='fangshou_grow',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='jingong',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='jingong_grow',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='qianzhi',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='qianzhi_grow',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='xintai',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='xintai_grow',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='yishi',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='yishi_grow',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='yunying',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='yunying_grow',
        ),
        migrations.RemoveField(
            model_name='stafflevel',
            name='quality_D',
        ),
        migrations.AddField(
            model_name='staff',
            name='lilun',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x90\x86\xe8\xae\xba'),
        ),
        migrations.AddField(
            model_name='staff',
            name='lilun_grow',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x90\x86\xe8\xae\xba\xe6\x88\x90\xe9\x95\xbf'),
        ),
        migrations.AddField(
            model_name='staff',
            name='luoji',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\x80\xbb\xe8\xbe\x91'),
        ),
        migrations.AddField(
            model_name='staff',
            name='luoji_grow',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\x80\xbb\xe8\xbe\x91\xe6\x88\x90\xe9\x95\xbf'),
        ),
        migrations.AddField(
            model_name='staff',
            name='meili',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\xad\x85\xe5\x8a\x9b'),
        ),
        migrations.AddField(
            model_name='staff',
            name='meili_grow',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\xad\x85\xe5\x8a\x9b\xe6\x88\x90\xe9\x95\xbf'),
        ),
        migrations.AddField(
            model_name='staff',
            name='minjie',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x95\x8f\xe6\x8d\xb7'),
        ),
        migrations.AddField(
            model_name='staff',
            name='minjie_grow',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x95\x8f\xe6\x8d\xb7\xe6\x88\x90\xe9\x95\xbf'),
        ),
        migrations.AddField(
            model_name='staff',
            name='wuxing',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x82\x9f\xe6\x80\xa7'),
        ),
        migrations.AddField(
            model_name='staff',
            name='wuxing_grow',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x82\x9f\xe6\x80\xa7\xe6\x88\x90\xe9\x95\xbf'),
        ),
        migrations.AddField(
            model_name='staffstatus',
            name='icon',
            field=models.CharField(max_length=255, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87', blank=True),
        ),
    ]
