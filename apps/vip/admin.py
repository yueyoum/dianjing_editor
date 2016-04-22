from django.contrib import admin
from django.dispatch import receiver

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.signals import post_import

from apps.vip.models import VIP

from misc import cache_set, create_fixture

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

@receiver(post_import, dispatch_uid='post_import.vip')
def _post_import(model, **kwargs):
    data = create_fixture('vip.VIP')
    cache_set('vip.VIP', data)
