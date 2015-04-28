from django.contrib import admin

from apps.training.models import TrainingType, Training

@admin.register(TrainingType)
class TrainingTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'tp', 'minutes', 'reward_type', 'reward_value'
    )
