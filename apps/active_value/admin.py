from django.contrib import admin

from apps.active_value.models import ActiveFunction, ActiveReward

@admin.register(ActiveFunction)
class ActiveFunctionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'value', 'max_times'
    )

@admin.register(ActiveReward)
class ActiveRewardAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'package'
    )
