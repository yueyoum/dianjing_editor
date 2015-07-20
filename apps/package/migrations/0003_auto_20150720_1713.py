# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_auto_20150720_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='attr_random_amount',
            field=models.IntegerField(default=1, help_text=b'\xe5\x8f\xaa\xe6\x9c\x89 \xe5\xb1\x9e\xe6\x80\xa7\xe6\xa8\xa1\xe5\xbc\x8f \xe4\xb8\xba \xe9\x9a\x8f\xe6\x9c\xba \xe6\x97\xb6\xef\xbc\x8c\xe6\x89\x8d\xe6\x9c\x89\xe7\x94\xa8', verbose_name=b'\xe9\x9a\x8f\xe6\x9c\xba\xe5\xb1\x9e\xe6\x80\xa7\xe6\x95\xb0\xe9\x87\x8f'),
        ),
    ]
