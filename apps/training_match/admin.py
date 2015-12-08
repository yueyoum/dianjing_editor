from django.contrib import admin

from apps.training_match.models import TrainingMatchReward

@admin.register(TrainingMatchReward)
class TrainingMatchRewardAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'reward', 'additional_reward', 'des'
    )
