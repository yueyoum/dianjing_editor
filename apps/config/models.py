from django.db import models

class ClientConfig(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.TextField()
    mean = models.CharField(max_length=255)

    class Meta:
        db_table = 'client_config'
        ordering = ('id',)


class GlobalConfig(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    value = models.IntegerField()
    mean = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'global_config'
