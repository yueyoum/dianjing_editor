# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0008_auto_20150818_1644'),
        ('building', '0011_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('icon', models.CharField(max_length=255, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87')),
                ('total_days', models.IntegerField(default=0, verbose_name=b'\xe5\x90\x88\xe7\xba\xa6\xe5\xa4\xa9\xe6\x95\xb0')),
                ('condition', models.ForeignKey(verbose_name=b'\xe9\x9c\x80\xe8\xa6\x81\xe9\x80\x9a\xe8\xbf\x87\xe7\x9a\x84\xe6\x8c\x91\xe6\x88\x98\xe8\xb5\x9b', to='match.ChallengeMatch')),
            ],
            options={
                'db_table': 'sponsor',
                'verbose_name': '\u8d5e\u52a9\u5546',
                'verbose_name_plural': '\u8d5e\u52a9\u5546',
            },
        ),
    ]
