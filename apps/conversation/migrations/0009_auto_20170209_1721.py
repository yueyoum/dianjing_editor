# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0008_auto_20160513_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationinfo',
            name='conversation',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.DeleteModel(
            name='ConversationInfo',
        ),
    ]