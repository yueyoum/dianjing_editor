# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qianban', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qianban',
            name='addition_tp',
            field=models.CharField(default='jingong', max_length=255, verbose_name=b'\xe5\x8a\xa0\xe6\x88\x90\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'jingong', b'\xe8\xbf\x9b\xe6\x94\xbb'), (b'qianzhi', b'\xe7\x89\xb5\xe5\x88\xb6'), (b'xintai', b'\xe5\xbf\x83\xe6\x80\x81'), (b'baobing', b'\xe6\x9a\xb4\xe5\x85\xb5'), (b'fangshou', b'\xe9\x98\xb2\xe5\xae\x88'), (b'yunying', b'\xe8\xbf\x90\xe8\x90\xa5'), (b'yishi', b'\xe6\x84\x8f\xe8\xaf\x86'), (b'caozuo', b'\xe6\x93\x8d\xe4\xbd\x9c'), (b'skill', b'\xe6\x8a\x80\xe8\x83\xbd\xe5\xbc\xba\xe5\xba\xa6')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qianban',
            name='addition_value',
            field=models.CommaSeparatedIntegerField(default='1', help_text=b'\xe5\xa6\x82\xe6\x9e\x9c\xe5\x8a\xa0\xe6\x88\x90\xe7\xb1\xbb\xe5\x9e\x8b\xe6\x98\xaf \xe6\x8a\x80\xe8\x83\xbd\xe5\xbc\xba\xe5\xba\xa6\xef\xbc\x8c\xe8\xbf\x99\xe9\x87\x8c\xe5\xa1\xab\xe5\x86\x99\xe7\x9a\x84\xe6\x98\xaf \xe6\x8a\x80\xe8\x83\xbdid,\xe5\xbc\xba\xe5\xba\xa6', max_length=255, verbose_name=b'\xe5\x8a\xa0\xe6\x88\x90\xe5\x80\xbc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qianban',
            name='condition_tp',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x9d\xa1\xe4\xbb\xb6', choices=[(1, b'\xe5\x90\x8c\xe6\x97\xb6\xe4\xb8\x8a\xe9\x98\xb5'), (2, b'\xe8\xa3\x85\xe9\x85\x8d\xe6\x8a\x80\xe8\x83\xbd')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qianban',
            name='condition_value',
            field=models.CommaSeparatedIntegerField(default='', help_text=b'id,id,id', max_length=255, verbose_name=b'\xe6\x9d\xa1\xe4\xbb\xb6\xe5\x80\xbc'),
            preserve_default=False,
        ),
    ]
