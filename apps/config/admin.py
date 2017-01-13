from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.config.models import ClientConfig, GlobalConfig

class ResourceCC(resources.ModelResource):
    class Meta:
        model = ClientConfig
        bulk_replace = True

class ResourceGC(resources.ModelResource):
    class Meta:
        model = GlobalConfig
        bulk_replace = True

@admin.register(ClientConfig)
class ClientConfigAdmin(ImportExportModelAdmin):
    resource_class = ResourceCC
    list_display = ('id', 'value', 'mean')

@admin.register(GlobalConfig)
class GlobalConfigAdmin(ImportExportModelAdmin):
    resource_class = ResourceGC
    list_display = ('id', 'value', 'value_string', 'mean')