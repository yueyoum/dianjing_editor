from django.contrib import admin

from apps.training.models import TrainingType, Training, TrainingProperty, TrainingSkill

@admin.register(TrainingType)
class TrainingTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'on_sell', 'tp', 'icon', 'des',
        'cost_type', 'cost_value', 'need_building_level',
        'minutes', 'package',
        'skill_id', 'skill_level',
    )


@admin.register(TrainingProperty)
class TrainingPropertyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon', 'des', 'minutes',
        'cost_type', 'cost_value', 'package', 'order_value'
    )

@admin.register(TrainingSkill)
class TrainingSkillAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon', 'des', 'minutes',
        'skill_id', 'skill_level'
    )
