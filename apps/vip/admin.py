from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.vip.models import VIP

class ResourceVIP(resources.ModelResource):
    class Meta:
        model = VIP
        bulk_replace = True


@admin.register(VIP)
class AdminVIP(ImportExportModelAdmin):
    resource_class = ResourceVIP

    list_display = (
        'id', 'exp',
        'item_id', 'diamond_original', 'diamond_now', 'item_preview',
        'des',
        'challenge_reset_times',
        'daily_dungeon_reset_times',
        'tower_reset_times',
        'arena_buy_times',
        'energy_buy_times',
        'store_refresh_times',
    )
