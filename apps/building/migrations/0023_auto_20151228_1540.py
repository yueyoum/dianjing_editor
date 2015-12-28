# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0022_auto_20151228_1533'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='shop',
            table='business_shop',
        ),
        migrations.AlterModelTable(
            name='sponsor',
            table='business_sponsor',
        ),
    ]
