# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0004_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationinfo',
            old_name='conversation_info',
            new_name='conversation',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='conversation',
        ),
        migrations.RemoveField(
            model_name='conversationinfo',
            name='contain',
        ),
        migrations.AddField(
            model_name='conversationinfo',
            name='message',
            field=models.TextField(default='', verbose_name=b'\xe4\xbc\x9a\xe8\xaf\x9d\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=False,
        ),
    ]
