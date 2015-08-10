from django.contrib import admin

from apps.function.models import Function

@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon',
        'belong_to_building',
        'order_in_building',
        'need_building_level',
        'unlock_des'
    )
