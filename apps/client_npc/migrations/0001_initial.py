# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientNPC',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('model', models.CharField(max_length=255, verbose_name=b'\xe6\xa8\xa1\xe5\x9e\x8b')),
                ('position', models.CharField(max_length=255, verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae')),
                ('function', models.IntegerField(default=0, verbose_name=b'\xe5\x8a\x9f\xe8\x83\xbd', choices=[(0, b'\xe6\xb2\xa1\xe6\x9c\x89\xe5\x8a\x9f\xe8\x83\xbd'), (1, b'\xe4\xbb\xbb\xe5\x8a\xa1')])),
                ('value', models.IntegerField(default=0, verbose_name=b'\xe5\x8a\x9f\xe8\x83\xbd\xe5\x80\xbc')),
            ],
            options={
                'db_table': 'client_npc',
                'verbose_name': '\u5ba2\u6237\u7aefNPC',
                'verbose_name_plural': '\u5ba2\u6237\u7aefNPC',
            },
        ),
        migrations.CreateModel(
            name='ClientNPCDiaLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dialog', models.TextField(verbose_name=b'\xe5\xaf\xb9\xe8\xaf\x9d')),
                ('npc', models.ForeignKey(to='client_npc.ClientNPC')),
            ],
            options={
                'db_table': 'client_npc_dialog',
            },
        ),
    ]
