from django.contrib import admin

from apps.formation.models import Slot

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ResourceSlot(resources.ModelResource):
    class Meta:
        model = Slot
        bulk_replace = True

@admin.register(Slot)
class AdminSlot(ImportExportModelAdmin):
    resource_class = ResourceSlot
    list_display = ('id', 'club_level', 'des')