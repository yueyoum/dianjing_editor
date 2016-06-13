from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.npc.models import NPCFormation

class ResourceNPCFormation(resources.ModelResource):
    class Meta:
        model = NPCFormation
        bulk_replace = True


@admin.register(NPCFormation)
class AdminNPCFormation(ImportExportModelAdmin):
    resource_class = ResourceNPCFormation

    list_display = (
        'id', 'staffs',
    )
