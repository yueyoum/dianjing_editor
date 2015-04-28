from django.contrib import admin

from apps.staff.models import (
    StaffQuality,
    StaffRace,
    StaffStatus,
    Staff,
)


@admin.register(StaffRace)
class StuffRaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(StaffQuality)
class StuffQualityAdmin(admin.ModelAdmin):
    list_display = ('id', 'color')

@admin.register(StaffStatus)
class StuffStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'des')


@admin.register(Staff)
class StuffAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'avatar', 'nation', 'race', 'quality',
        'buy_cost', 'des',
    )

    list_filter = ('race', 'quality')
