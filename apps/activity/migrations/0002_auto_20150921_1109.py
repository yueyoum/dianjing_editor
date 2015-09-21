# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_auto_20150910_1735'),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLoginReward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.IntegerField(verbose_name=b'\xe7\xac\xac\xe5\x87\xa0\xe5\xa4\xa9\xe7\x99\xbb\xe5\xbd\x95')),
                ('activity', models.ForeignKey(verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8', to='activity.Activity')),
                ('package', models.ForeignKey(verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1', to='package.Package')),
            ],
            options={
                'db_table': 'activity_login_reward',
                'verbose_name': '\u6d3b\u52a8 - \u65b0\u73a9\u5bb6\u6709\u793c',
                'verbose_name_plural': '\u6d3b\u52a8 - \u65b0\u73a9\u5bb6\u6709\u793c',
            },
        ),
        migrations.AddField(
            model_name='activitycategory',
            name='mode',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\xa5\x96\xe5\x8a\xb1\xe6\xa8\xa1\xe5\xbc\x8f', choices=[(1, b'\xe6\x89\x8b\xe5\x8a\xa8\xe9\xa2\x86\xe5\x8f\x96'), (2, b'\xe7\xb3\xbb\xe7\xbb\x9f\xe9\x82\xae\xe4\xbb\xb6')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activitysignin',
            name='activity',
            field=models.OneToOneField(verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8', to='activity.Activity'),
        ),
    ]
