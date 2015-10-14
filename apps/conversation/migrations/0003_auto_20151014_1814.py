# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0002_auto_20151014_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(verbose_name=b'\xe4\xbc\x9a\xe8\xaf\x9d\xe8\x80\x85\xe4\xbd\x8d\xe7\xbd\xae', choices=[(1, b'\xe5\x9c\xa8\xe5\xb7\xa6\xe8\xbe\xb9'), (2, b'\xe5\x9c\xa8\xe5\x8f\xb3\xe8\xbe\xb9')])),
                ('icon', models.CharField(max_length=255, verbose_name=b'\xe4\xbc\x9a\xe8\xaf\x9d\xe8\x80\x85\xe5\x9b\xbe\xe6\xa0\x87')),
                ('contain', models.CharField(max_length=255, verbose_name=b'\xe4\xbc\x9a\xe8\xaf\x9d\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'db_table': 'conversation_info',
            },
        ),
        migrations.AlterField(
            model_name='conversation',
            name='conversation',
            field=models.TextField(verbose_name=b'\xe5\x89\xa7\xe6\x83\x85', blank=True),
        ),
        migrations.AddField(
            model_name='conversationinfo',
            name='conversation_info',
            field=models.ForeignKey(to='conversation.Conversation'),
        ),
    ]
