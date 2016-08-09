# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class FirstName(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'first_name'
        verbose_name = '姓'
        verbose_name_plural = '姓'


class LastName(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'last_name'
        verbose_name = '名'
        verbose_name_plural = '名'