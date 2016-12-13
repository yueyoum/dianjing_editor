from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.championship.models import (
    ChampionshipWinScore,
    ChampionshipScoreReward,
    ChampionshipRankReward,
    ChampionshipBet,
)

class ResourceWS(resources.ModelResource):
    class Meta:
        model = ChampionshipWinScore
        bulk_replace = True

class ResourceSR(resources.ModelResource):
    class Meta:
        model = ChampionshipScoreReward
        bulk_replace = True

class ResourceRR(resources.ModelResource):
    class Meta:
        model = ChampionshipRankReward
        bulk_replace = True

class ResourceBet(resources.ModelResource):
    class Meta:
        model = ChampionshipBet
        bulk_replace = True

@admin.register(ChampionshipWinScore)
class AdminWS(ImportExportModelAdmin):
    resource_class = ResourceWS
    list_display = ('id', 'score')

@admin.register(ChampionshipScoreReward)
class AdminSR(ImportExportModelAdmin):
    resource_class = ResourceSR
    list_display = ('id', 'mail_title', 'mail_content', 'reward')

@admin.register(ChampionshipRankReward)
class AdminRR(ImportExportModelAdmin):
    resource_class = ResourceRR
    list_display = ('id', 'mail_title', 'mail_content', 'reward')

@admin.register(ChampionshipBet)
class AdminBet(ImportExportModelAdmin):
    resource_class = ResourceBet
    list_display = (
        'id', 'name', 'round_num', 'cost',
        'win_mail_title', 'win_mail_content', 'win_reward',
        'lose_mail_title', 'lose_mail_content', 'lose_reward',
    )
