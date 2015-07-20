# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='attr_random_value',
            field=models.CharField(help_text=b'\xe5\x8f\xaa\xe6\x9c\x89 \xe5\xb1\x9e\xe6\x80\xa7\xe6\xa8\xa1\xe5\xbc\x8f \xe4\xb8\xba \xe5\xae\x8c\xe5\x85\xa8\xe9\x9a\x8f\xe6\x9c\xba \xe6\x97\xb6\xef\xbc\x8c\xe6\x89\x8d\xe6\x9c\x89\xe7\x94\xa8', max_length=32, verbose_name=b'\xe9\x9a\x8f\xe6\x9c\xba\xe5\xb1\x9e\xe6\x80\xa7\xe5\x80\xbc\xe8\x8c\x83\xe5\x9b\xb4', blank=True),
        ),
    ]
