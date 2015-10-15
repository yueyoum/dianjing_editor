from django.contrib import admin

from apps.item.models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon', 'des',
        'buy_type', 'buy_cost',
        'sell_gold'
    )
