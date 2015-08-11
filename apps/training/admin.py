from django.contrib import admin

from apps.training.models import TrainingType, Training

@admin.register(TrainingType)
class TrainingTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'on_sell', 'tp', 'icon', 'des',
        'cost_type', 'cost_value', 'need_building_level',
        'minutes', 'package',
    )
