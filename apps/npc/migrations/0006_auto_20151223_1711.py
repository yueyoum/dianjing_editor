# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('npc', '0005_npcclub_league'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='npcclub',
            name='baobing_high',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='baobing_low',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='caozuo_high',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='caozuo_low',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='fangshou_high',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='fangshou_low',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='jingong_high',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='jingong_low',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='qianzhi_high',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='qianzhi_low',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='skill_high',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='skill_low',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='xintai_high',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='xintai_low',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='yishi_high',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='yishi_low',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='yunying_high',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='yunying_low',
        ),
        migrations.AddField(
            model_name='npcclub',
            name='baobing',
            field=models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe6\x9a\xb4\xe5\x85\xb5\xe8\x8c\x83\xe5\x9b\xb4', blank=True),
        ),
        migrations.AddField(
            model_name='npcclub',
            name='caozuo',
            field=models.CommaSeparatedIntegerField(help_text=b'low,high', max_length=255, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe8\x8c\x83\xe5\x9b\xb4', blank=True),
        ),
        migrations.AddField(
            model_name='npcclub',
            name='skill_level',
            field=models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd\xe7\xad\x89\xe7\xba\xa7\xe8\x8c\x83\xe5\x9b\xb4', blank=True),
        ),
        migrations.AddField(
            model_name='npcclub',
            name='yunying',
            field=models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe8\xbf\x90\xe8\x90\xa5\xe8\x8c\x83\xe5\x9b\xb4', blank=True),
        ),
        migrations.AddField(
            model_name='npcclub',
            name='zhanshu',
            field=models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe6\x88\x98\xe6\x9c\xaf\xe8\x8c\x83\xe5\x9b\xb4', blank=True),
        ),
    ]
