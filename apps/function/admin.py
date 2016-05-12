from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.function.models import Function

class ResourceFunction(resources.ModelResource):
    class Meta:
        model = Function


@admin.register(Function)
class FunctionAdmin(ImportExportModelAdmin):
    resource_class = ResourceFunction

    list_display = (
        'id', 'name', 'icon',
        'belong_to_building',
        'belong_to_ui',
        'order_in_building',
        'need_building_level',
        'need_challenge_id',
        'unlock_des'
    )
