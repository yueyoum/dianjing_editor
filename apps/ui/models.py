from __future__ import unicode_literals

from django.db import models

class UI(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    icon = models.CharField(max_length=255)
    des = models.TextField()

    class Meta:
        db_table = 'ui'