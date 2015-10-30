# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0006_auto_20151028_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='picture',
            field=models.CharField(default='', max_length=255, verbose_name=b'\xe5\xb0\x8f\xe7\xa7\x98\xe4\xb9\xa6\xe5\x9b\xbe\xe7\x89\x87'),
            preserve_default=False,
        ),
    ]
