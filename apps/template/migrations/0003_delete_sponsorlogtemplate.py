# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0002_broadcasttemplate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SponsorLogTemplate',
        ),
    ]