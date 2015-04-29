from django.contrib import admin

from apps.config.models import ClientConfig

@admin.register(ClientConfig)
class ClientConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
