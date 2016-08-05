from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.activity.models import NewPlayerActivity, DailyBuy

class ResourceNewPlayer(resources.ModelResource):
    class Meta:
        model = NewPlayerActivity
        bulk_replace = True

class ResourceDailyBuy(resources.ModelResource):
    class Meta:
        model = DailyBuy
        bulk_replace = True


@admin.register(NewPlayerActivity)
class AdminNewPlayer(ImportExportModelAdmin):
    resource_class = ResourceNewPlayer
    list_display = (
        'id', 'day', 'name',
        'condition_id', 'condition_value',
        'rewards', 'show_progress'
    )

@admin.register(DailyBuy)
class AdminDailyBuy(ImportExportModelAdmin):
    resource_class = ResourceDailyBuy
    list_display = (
        'id', 'items', 'diamond_original', 'diamond_now'
    )