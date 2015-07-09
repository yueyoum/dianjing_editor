# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_staffstatus_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffHot',
            fields=[
                ('id', models.OneToOneField(primary_key=True, serialize=False, to='staff.Staff', verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5')),
                ('cost', models.IntegerField(verbose_name=b'\xe8\x8a\xb1\xe8\xb4\xb9')),
            ],
            options={
                'db_table': 'staff_hot',
                'verbose_name': '\u5458\u5de5\u62db\u52df-\u4eba\u6c14\u738b',
                'verbose_name_plural': '\u5458\u5de5\u62db\u52df-\u4eba\u6c14\u738b',
            },
        ),
        migrations.CreateModel(
            name='StaffRecruit',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('cost_type', models.IntegerField(verbose_name=b'\xe8\x8a\xb1\xe8\xb4\xb9\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'RMB'), (2, b'\xe9\x92\xbb\xe7\x9f\xb3')])),
                ('cost_value', models.IntegerField(verbose_name=b'\xe8\x8a\xb1\xe8\xb4\xb9\xe9\x87\x91\xe9\xa2\x9d')),
                ('lucky_times', models.IntegerField(verbose_name=b'\xe5\xb9\xb8\xe8\xbf\x90\xe6\xac\xa1\xe6\x95\xb0')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'db_table': 'staff_recruit',
                'verbose_name': '\u5458\u5de5\u62db\u52df-\u5408\u7ea6',
                'verbose_name_plural': '\u5458\u5de5\u62db\u52df-\u5408\u7ea6',
            },
        ),
        migrations.CreateModel(
            name='StaffRecruitSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_amount', models.IntegerField(verbose_name=b'\xe9\xa6\x96\xe6\xac\xa1\xe5\x88\xb7\xe6\x96\xb0\xe5\x87\xba\xe7\x8e\xb0\xe6\xac\xa1\xe6\x95\xb0')),
                ('lucky_amount', models.IntegerField(verbose_name=b'\xe5\xb9\xb8\xe8\xbf\x90\xe5\x88\xb7\xe6\x96\xb0\xe5\x87\xba\xe7\x8e\xb0\xe6\xac\xa1\xe6\x95\xb0')),
                ('normal_amount', models.IntegerField(verbose_name=b'\xe5\xb9\xb3\xe6\x97\xb6\xe5\x87\xba\xe7\x8e\xb0\xe6\xac\xa1\xe6\x95\xb0')),
                ('ids', models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe5\x91\x98\xe5\xb7\xa5ID\xe5\x88\x97\xe8\xa1\xa8')),
                ('quality', models.ForeignKey(verbose_name=b'\xe5\x93\x81\xe8\xb4\xa8', to='staff.StaffQuality')),
                ('recruit', models.ForeignKey(to='staff.StaffRecruit')),
            ],
            options={
                'db_table': 'staff_recruit_settings',
            },
        ),
        migrations.AddField(
            model_name='staffrecruit',
            name='recruit_settings',
            field=models.ManyToManyField(to='staff.StaffRecruitSettings'),
        ),
    ]
