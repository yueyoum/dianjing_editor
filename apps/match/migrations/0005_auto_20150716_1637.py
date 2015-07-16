# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_auto_20150710_1608'),
        ('unit', '0003_auto_20150713_1639'),
        ('match', '0004_auto_20150716_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchConversationEnd',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('end_at', models.IntegerField(verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe4\xba\x8e', choices=[(1, b'\xe7\xac\xac\xe4\xb8\x80\xe5\x9b\x9e\xe5\x90\x88'), (2, b'\xe7\xac\xac\xe4\xba\x8c\xe5\x9b\x9e\xe5\x90\x88'), (3, b'\xe7\xac\xac\xe4\xb8\x89\xe5\x9b\x9e\xe5\x90\x88')])),
                ('disadvantage_win', models.BooleanField(default=False, verbose_name=b'\xe5\x8a\xa3\xe5\x8a\xbf\xe6\x96\xb9\xe6\x98\xaf\xe5\x90\xa6\xe8\x83\x9c\xe5\x88\xa9')),
                ('disadvantage_value', models.IntegerField(verbose_name=b'\xe5\x8a\xa3\xe5\x8a\xbf\xe6\x96\xb9\xe4\xbc\x98\xe5\x8a\xbf\xe5\x80\xbc', choices=[(50, b'=50'), (49, b'40<=, <50'), (39, b'30<=, <40'), (29, b'20<=, <30'), (19, b'10<=, <20'), (9, b'0<=, <10')])),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'db_table': 'match_conversation_end',
                'verbose_name': '\u6bcf\u5c40\u6bd4\u8d5b\u7ed3\u675f\u5bf9\u8bdd',
                'verbose_name_plural': '\u6bcf\u5c40\u6bd4\u8d5b\u7ed3\u675f\u5bf9\u8bdd',
            },
        ),
        migrations.CreateModel(
            name='MatchConversationRoundEnd',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe7\xac\xac\xe5\x87\xa0\xe5\x9b\x9e\xe5\x90\x88', primary_key=True, choices=[(1, b'\xe7\xac\xac\xe4\xb8\x80\xe5\x9b\x9e\xe5\x90\x88'), (2, b'\xe7\xac\xac\xe4\xba\x8c\xe5\x9b\x9e\xe5\x90\x88'), (3, b'\xe7\xac\xac\xe4\xb8\x89\xe5\x9b\x9e\xe5\x90\x88')])),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'db_table': 'match_conversation_round_end',
                'verbose_name': '\u6bcf\u56de\u5408\u6bd4\u8d5b\u7ed3\u675f\u5bf9\u8bdd',
                'verbose_name_plural': '\u6bcf\u56de\u5408\u6bd4\u8d5b\u7ed3\u675f\u5bf9\u8bdd',
            },
        ),
        migrations.CreateModel(
            name='MatchConversationStart',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('policy', models.ForeignKey(verbose_name=b'\xe6\x88\x98\xe6\x9c\xaf', to='unit.Policy')),
                ('race', models.ForeignKey(verbose_name=b'\xe7\xa7\x8d\xe6\x97\x8f', to='staff.StaffRace')),
            ],
            options={
                'db_table': 'match_conversation_start',
                'verbose_name': '\u6bcf\u5c40\u6bd4\u8d5b\u5f00\u59cb\u5bf9\u8bdd',
                'verbose_name_plural': '\u6bcf\u5c40\u6bd4\u8d5b\u5f00\u59cb\u5bf9\u8bdd',
            },
        ),
        migrations.AddField(
            model_name='challengematch',
            name='des',
            field=models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
    ]
