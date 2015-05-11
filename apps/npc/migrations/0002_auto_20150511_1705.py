# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('npc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npcclub',
            name='baobing_high',
            field=models.IntegerField(verbose_name=b'\xe6\x9a\xb4\xe5\x85\xb5\xe4\xb8\x8a\xe9\x99\x90'),
        ),
        migrations.AlterField(
            model_name='npcclub',
            name='caozuo_high',
            field=models.IntegerField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe4\xb8\x8a\xe9\x99\x90'),
        ),
        migrations.AlterField(
            model_name='npcclub',
            name='fangshou_high',
            field=models.IntegerField(verbose_name=b'\xe9\x98\xb2\xe5\xae\x88\xe4\xb8\x8a\xe9\x99\x90'),
        ),
        migrations.AlterField(
            model_name='npcclub',
            name='jingong_high',
            field=models.IntegerField(verbose_name=b'\xe8\xbf\x9b\xe6\x94\xbb\xe4\xb8\x8a\xe9\x99\x90'),
        ),
        migrations.AlterField(
            model_name='npcclub',
            name='qianzhi_high',
            field=models.IntegerField(verbose_name=b'\xe7\x89\xb5\xe5\x88\xb6\xe4\xb8\x8a\xe9\x99\x90'),
        ),
        migrations.AlterField(
            model_name='npcclub',
            name='xintai_high',
            field=models.IntegerField(verbose_name=b'\xe5\xbf\x83\xe6\x80\x81\xe4\xb8\x8a\xe9\x99\x90'),
        ),
        migrations.AlterField(
            model_name='npcclub',
            name='yishi_high',
            field=models.IntegerField(verbose_name=b'\xe6\x84\x8f\xe8\xaf\x86\xe4\xb8\x8a\xe9\x99\x90'),
        ),
        migrations.AlterField(
            model_name='npcclub',
            name='yunying_high',
            field=models.IntegerField(verbose_name=b'\xe8\xbf\x90\xe8\x90\xa5\xe4\xb8\x8a\xe9\x99\x90'),
        ),
    ]
