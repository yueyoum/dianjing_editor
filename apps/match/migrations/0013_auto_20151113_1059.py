# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0012_remove_challengematch_next_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengematch',
            name='need_club_level',
            field=models.IntegerField(default=1, verbose_name=b'\xe9\x9c\x80\xe8\xa6\x81\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe7\xad\x89\xe7\xba\xa7'),
        ),
        migrations.AlterField(
            model_name='challengematch',
            name='club_flag',
            field=models.ForeignKey(verbose_name=b'\xe5\x85\xb3\xe5\x8d\xa1\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe6\x97\x97\xe5\xb8\x9c', to='club.ClubFlag'),
        ),
        migrations.AlterField(
            model_name='challengematch',
            name='club_name',
            field=models.CharField(max_length=255, verbose_name=b'\xe5\x85\xb3\xe5\x8d\xa1\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe5\x90\x8d\xe5\xad\x97'),
        ),
    ]
