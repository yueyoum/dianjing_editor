from django.contrib import admin

from apps.config.models import ClientConfig, GlobalConfig

@admin.register(ClientConfig)
class ClientConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'mean')

@admin.register(GlobalConfig)
class GlobalConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'mean')