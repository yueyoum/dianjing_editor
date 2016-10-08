from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.function.models import Function, FunctionTips

class ResourceFunction(resources.ModelResource):
    class Meta:
        model = Function
        bulk_replace = True

class ResourceFT(resources.ModelResource):
    class Meta:
        model = FunctionTips
        bulk_replace = True


@admin.register(Function)
class FunctionAdmin(ImportExportModelAdmin):
    resource_class = ResourceFunction

    list_display = (
        'id', 'name', 'icon',
        'belong_to_building',
        'belong_to_ui',
        'order_in_building',
        'need_club_level',
        'need_challenge_id',
        'unlock_des',
        'normal_color',
        'lock_color',
    )

@admin.register(FunctionTips)
class AdminFT(ImportExportModelAdmin):
    resource_class = ResourceFT
    list_display = (
        'id', 'level', 'tp', 'target', 'des'
    )