from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.vip.models import VIP

class ResourceVIP(resources.ModelResource):
    class Meta:
        model = VIP

@admin.register(VIP)
class AdminVIP(ImportExportModelAdmin):
    resource_class = ResourceVIP

    list_display = (
        'id', 'update_vip_exp',
        'item_id', 'diamond_original', 'diamond_now', 'item_preview',
        'des',
    )
