# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('active_value', '0003_activereward_des'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activefunction',
            old_name='function_sign',
            new_name='function_name',
        ),
        migrations.AlterField(
            model_name='activefunction',
            name='id',
            field=models.CharField(max_length=255, serialize=False, verbose_name=b'\xe5\x8a\x9f\xe8\x83\xbd', primary_key=True),
        ),
    ]
