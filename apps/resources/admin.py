from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.resources.models import Resource

class RR(resources.ModelResource):
    class Meta:
        model = Resource
        bulk_replace = True


@admin.register(Resource)
class ResourceAdmin(ImportExportModelAdmin):
    resource_class = RR

    list_display = (
        'id', 'name', 'icon'
    )
