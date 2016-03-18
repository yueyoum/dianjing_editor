from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.match.models import (
    ChallengeMatch,
    ChallengeChapter,
    MatchConversationEnd,
    MatchConversationRoundEnd,
    MatchConversationStart,
    Maps,
    TrainingMatchReward,
    TrainingMatchScoreStore,
    EliteArea,
    EliteMatch,
)

class ResourceChallengeChapter(resources.ModelResource):
    class Meta:
        model = ChallengeChapter


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


@admin.register(ChallengeChapter)
class ChallengeTypeAdmin(ImportExportModelAdmin):
    resource_class = ResourceChallengeChapter
    list_display = (
        'id', 'name', 'icon', 'des'
    )

@admin.register(ChallengeMatch)
class ChallengeMatchAdmin(ImportExportModelAdmin):
    resource_class = ChallengeMatchResource

    list_display = (
        'id', 'tp', 'area', 'chapter', 'name',
    )

    list_filter = ('chapter',)

@admin.register(Maps)
class MapsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'picture',
    )



@admin.register(TrainingMatchReward)
class TrainingMatchRewardAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'reward', 'score', 'des'
    )


@admin.register(TrainingMatchScoreStore)
class TrainingMatchScoreStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'times_limit', 'score',
                    'item', 'item_amount',
                    )


@admin.register(EliteArea)
class EliteAreaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'need_club_level', 'match_ids',
        'map_name', 'des', 'star_reward',
    )

@admin.register(EliteMatch)
class EliteMatchAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'max_times', 'club_name',
        'club_flag', 'policy', 'staff_level', 'staffs',
        'reward', 'des'
    )
