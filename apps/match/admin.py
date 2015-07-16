from django.contrib import admin

from apps.match.models import (
    ChallengeType,
    ChallengeMatch,
    MatchConversationEnd,
    MatchConversationRoundEnd,
    MatchConversationStart
)


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
        'id', 'name', 'level', 'des'
    )


@admin.register(ChallengeMatch)
class ChallengeMatchAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'next_id', 'name', 'club_name', 'club_flag', 'tp', 'policy', 'level', 'strength', 'staffs',
        'des'
    )

    list_filter = ('tp',)
