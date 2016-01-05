from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.item.models import Item


class ItemResource(resources.ModelResource):
    class Meta:
        model = Item

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource

    list_display = (
        'id', 'tp', 'sub_tp', 'name', 'icon', 'quality',
        'des',
        'buy_type', 'buy_cost',
        'sell_gold',
        'order_value',
        'value',
    )

    list_filter = ('tp',)

    change_list_template = 'item_change_list.html'
