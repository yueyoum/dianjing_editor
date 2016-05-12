from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.building.models import (
    BuildingNew
)


class ResourceBuildingNew(resources.ModelResource):
    class Meta:
        model = BuildingNew

@admin.register(BuildingNew)
class AdminBuildingNew(ImportExportModelAdmin):
    resource_class = ResourceBuildingNew
    list_display = (
        'id', 'name', 'des', 'effect_day', 'effect_night', 'model_resource', 'position'
    )