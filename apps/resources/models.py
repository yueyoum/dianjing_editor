# -*- coding: utf-8 -*-

from django.db import models

class Resource(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'resource'
        verbose_name = "资源"
        verbose_name_plural = "资源"
