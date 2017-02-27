from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.ui.models import UI, BackgroundImage

class ResourceUI(resources.ModelResource):
    class Meta:
        model = UI
        bulk_replace = True

class ResourceBI(resources.ModelResource):
    class Meta:
        model = BackgroundImage
        bulk_replace = True

@admin.register(UI)
class AdminUI(ImportExportModelAdmin):
    resource_class = ResourceUI
    list_display = ('id', 'icon', 'des')

@admin.register(BackgroundImage)
class AdminBI(ImportExportModelAdmin):
    resource_class = ResourceBI
    list_display = ('id', 'image')