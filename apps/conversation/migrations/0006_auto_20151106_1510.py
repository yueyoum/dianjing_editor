# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0005_auto_20151015_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationinfo',
            old_name='message',
            new_name='dialog',
        ),
    ]
