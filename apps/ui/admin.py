from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.ui.models import UI

class ResourceUI(resources.ModelResource):
    class Meta:
        model = UI
        bulk_replace = True

@admin.register(UI)
class AdminUI(ImportExportModelAdmin):
    resource_class = ResourceUI
    list_display = ('id', 'icon', 'des')
