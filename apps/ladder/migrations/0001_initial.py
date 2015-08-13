# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0006_remove_package_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='LadderLogTemplate',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('template', models.CharField(max_length=255, verbose_name=b'\xe6\xa8\xa1\xe6\x9d\xbf')),
            ],
            options={
                'db_table': 'ladder_log_template',
                'verbose_name': '\u5929\u68af\u6218\u51b5\u6a21\u677f',
                'verbose_name_plural': '\u5929\u68af\u6218\u51b5\u6a21\u677f',
            },
        ),
        migrations.CreateModel(
            name='LadderRankReward',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe6\x8e\x92\xe5\x90\x8d\xe4\xb8\x8a\xe9\x99\x90', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('score', models.IntegerField(verbose_name=b'\xe7\xa7\xaf\xe5\x88\x86')),
                ('reward_des', models.TextField(verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('package', models.ForeignKey(verbose_name=b'\xe7\x89\xa9\xe5\x93\x81\xe5\x8c\x85', blank=True, to='package.Package', null=True)),
            ],
            options={
                'db_table': 'ladder_rank_reward',
                'verbose_name': '\u5929\u68af\u6392\u540d\u5956\u52b1',
                'verbose_name_plural': '\u5929\u68af\u6392\u540d\u5956\u52b1',
            },
        ),
        migrations.CreateModel(
            name='LadderScoreStore',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('times_limit', models.IntegerField(default=-1, help_text=b'-1\xe4\xb8\xba\xe6\xb2\xa1\xe6\x9c\x89\xe9\x99\x90\xe5\x88\xb6\xef\xbc\x8c0\xe4\xb8\xba\xe6\x97\xa0\xe6\xb3\x95\xe5\x85\x91\xe6\x8d\xa2\xef\xbc\x8c\xe6\xad\xa3\xe6\x95\xb4\xe6\x95\xb0N\xe8\xa1\xa8\xe7\xa4\xba\xe5\x8f\xaf\xe4\xbb\xa5\xe5\x85\x91\xe6\x8d\xa2N\xe6\xac\xa1', verbose_name=b'\xe6\xac\xa1\xe6\x95\xb0\xe9\x99\x90\xe5\x88\xb6')),
                ('score', models.IntegerField(verbose_name=b'\xe6\x89\x80\xe9\x9c\x80\xe7\xa7\xaf\xe5\x88\x86')),
                ('package', models.ForeignKey(verbose_name=b'\xe7\x89\xa9\xe5\x93\x81\xe5\x8c\x85', to='package.Package')),
            ],
            options={
                'db_table': 'ladder_score_store',
                'verbose_name': '\u5929\u68af\u79ef\u5206\u5546\u5e97',
                'verbose_name_plural': '\u5929\u68af\u79ef\u5206\u5546\u5e97',
            },
        ),
    ]
