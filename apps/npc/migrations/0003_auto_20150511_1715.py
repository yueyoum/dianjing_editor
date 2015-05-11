# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('npc', '0002_auto_20150511_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='NPCClubName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'npc_club_name',
                'verbose_name': 'NPC\u4ff1\u4e50\u90e8\u540d\u5b57',
                'verbose_name_plural': 'NPC\u4ff1\u4e50\u90e8\u540d\u5b57',
            },
        ),
        migrations.CreateModel(
            name='NPCManagerName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'npc_manager_name',
                'verbose_name': 'NPC\u7ecf\u7406\u4eba\u540d\u5b57',
                'verbose_name_plural': 'NPC\u7ecf\u7406\u4eba\u540d\u5b57',
            },
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='manager_name',
        ),
        migrations.RemoveField(
            model_name='npcclub',
            name='name',
        ),
    ]
