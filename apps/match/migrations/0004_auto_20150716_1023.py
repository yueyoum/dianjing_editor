# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20150716_1023'),
        ('match', '0003_challengematch_policy'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengematch',
            name='club_flag',
            field=models.ForeignKey(default=1, verbose_name=b'\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe6\x97\x97\xe5\xb8\x9c', to='club.ClubFlag'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challengematch',
            name='club_name',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe5\x90\x8d\xe5\xad\x97'),
            preserve_default=False,
        ),
    ]
