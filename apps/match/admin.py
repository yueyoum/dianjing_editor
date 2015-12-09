from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.match.models import (
    ChallengeType,
    ChallengeMatch,
    MatchConversationEnd,
    MatchConversationRoundEnd,
    MatchConversationStart,
    Maps,
    TrainingMatchReward,
    EliteArea,
    EliteMatch,
)

class ChallengeMatchResource(resources.ModelResource):
    class Meta:
        model = ChallengeMatch


@admin.register(MatchConversationStart)
class MatchConversationStartAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'policy', 'race', 'des'
    )

@admin.register(MatchConversationEnd)
class MatchConversationEndAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'end_at', 'disadvantage_win', 'disadvantage_value',
        'des'
    )

@admin.register(MatchConversationRoundEnd)
class MatchConversationRoundEndAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'des'
    )


@admin.register(ChallengeType)
class ChallengeTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'condition_challenge_id', 'level', 'color', 'des'
    )


@admin.register(ChallengeMatch)
class ChallengeMatchAdmin(ImportExportModelAdmin):
    resource_class = ChallengeMatchResource

    list_display = (
        'id', 'name', 'need_club_level', 'club_name', 'club_flag', 'tp', 'policy', 'level', 'strength', 'staffs',
        'winning_rates',
        'package',
        'des'
    )

    list_filter = ('tp',)

@admin.register(Maps)
class MapsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'picture',
    )



@admin.register(TrainingMatchReward)
class TrainingMatchRewardAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'reward', 'additional_reward', 'des'
    )

@admin.register(EliteArea)
class EliteAreaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'need_club_level', 'match_ids',
        'map_name', 'des'
    )

@admin.register(EliteMatch)
class EliteMatchAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'max_times', 'club_name',
        'club_flag', 'policy', 'staff_level', 'staffs',
        'reward', 'des'
    )
