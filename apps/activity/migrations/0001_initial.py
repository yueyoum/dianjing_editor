# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_auto_20150910_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'db_table': 'activity',
                'verbose_name': '\u6d3b\u52a8',
                'verbose_name_plural': '\u6d3b\u52a8',
            },
        ),
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('fixed', models.BooleanField(default=False, help_text=b'\xe5\x9b\xba\xe5\xae\x9a\xe6\xb4\xbb\xe5\x8a\xa8\xe4\xb8\x8d\xe7\x94\xa8\xe8\xae\xbe\xe7\xbd\xae\xe4\xb8\x8b\xe9\x9d\xa2\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4', verbose_name=b'\xe5\x9b\xba\xe5\xae\x9a\xe6\xb4\xbb\xe5\x8a\xa8')),
                ('start_at', models.DateTimeField(null=True, verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('end_at', models.DateTimeField(null=True, verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'db_table': 'activity_category',
                'verbose_name': '\u6d3b\u52a8\u5206\u7c7b',
                'verbose_name_plural': '\u6d3b\u52a8\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='ActivitySignIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valid_test_divisor', models.IntegerField(default=1, verbose_name=b'\xe6\x9c\x89\xe6\x95\x88\xe6\xb5\x8b\xe8\xaf\x95 \xe9\x99\xa4\xe6\x95\xb0')),
                ('valid_test_value', models.IntegerField(default=0, help_text=b'day % \xe9\x99\xa4\xe6\x95\xb0 == \xe5\x80\xbc \xe4\xb8\xba\xe6\x9c\x89\xe6\x95\x88', verbose_name=b'\xe6\x9c\x89\xe6\x95\x88\xe6\xb5\x8b\xe8\xaf\x95 \xe5\x80\xbc')),
                ('circle_times', models.IntegerField(verbose_name=b'\xe7\xac\xac\xe5\x87\xa0\xe6\xac\xa1\xe7\xad\xbe\xe5\x88\xb0\xe7\xbb\x99\xe5\xa4\xa7\xe5\xa5\x96')),
                ('mail_title', models.CharField(max_length=255, verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe6\xa0\x87\xe9\xa2\x98')),
                ('mail_content', models.TextField(verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe5\x86\x85\xe5\xae\xb9')),
                ('activity', models.OneToOneField(to='activity.Activity')),
                ('circle_package', models.ForeignKey(verbose_name=b'\xe5\xa4\xa7\xe5\xa5\x96', to='package.Package')),
            ],
            options={
                'db_table': 'activity_signin',
                'verbose_name': '\u6d3b\u52a8 - \u7b7e\u5230',
                'verbose_name_plural': '\u6d3b\u52a8 - \u7b7e\u5230',
            },
        ),
        migrations.CreateModel(
            name='ActivitySignInDayReward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.IntegerField(verbose_name=b'\xe7\xac\xac\xe5\x87\xa0\xe5\xa4\xa9')),
                ('activity_signin', models.ForeignKey(to='activity.ActivitySignIn')),
                ('package', models.ForeignKey(verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1', to='package.Package')),
            ],
            options={
                'db_table': 'activity_signin_day_reward',
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='activity.ActivityCategory'),
        ),
    ]
