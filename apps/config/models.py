from django.db import models

class ClientConfig(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.TextField()
    mean = models.CharField(max_length=255)

    class Meta:
        db_table = 'client_config'
        ordering = ('id',)
