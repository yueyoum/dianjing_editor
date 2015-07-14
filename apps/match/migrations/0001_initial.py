# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeMatch',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('level', models.IntegerField(verbose_name=b'\xe9\x80\x89\xe6\x89\x8b\xe7\xad\x89\xe7\xba\xa7')),
                ('strength', models.FloatField(verbose_name=b'\xe9\x80\x89\xe6\x89\x8b\xe5\xbc\xba\xe5\xba\xa6\xe7\xb3\xbb\xe6\x95\xb0')),
                ('staffs', models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'\xe9\x80\x89\xe6\x89\x8bID\xe5\x88\x97\xe8\xa1\xa8')),
            ],
            options={
                'db_table': 'challenge_match',
                'verbose_name': '\u6311\u6218\u8d5b',
                'verbose_name_plural': '\u6311\u6218\u8d5b',
            },
        ),
        migrations.CreateModel(
            name='ChallengeType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('level', models.IntegerField(verbose_name=b'\xe7\xad\x89\xe7\xba\xa7')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'db_table': 'challenge_type',
                'verbose_name': '\u6311\u6218\u8d5b\u7c7b\u578b',
                'verbose_name_plural': '\u6311\u6218\u8d5b\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='challengematch',
            name='tp',
            field=models.ForeignKey(verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', to='match.ChallengeType'),
        ),
    ]
