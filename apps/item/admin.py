from django.contrib import admin

from apps.item.models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'tp', 'name', 'icon', 'quality',
        'des',
        'buy_type', 'buy_cost',
        'sell_gold',
        'order_value',
        'value',
    )

    list_filter = ('tp',)
