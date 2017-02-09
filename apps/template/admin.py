from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.template.models import BroadcastTemplate

class ResourceBT(resources.ModelResource):
    class Meta:
        model = BroadcastTemplate
        bulk_replace = True

@admin.register(BroadcastTemplate)
class AdminBT(ImportExportModelAdmin):
    resource_class = ResourceBT
    list_display = ('id', 'template')