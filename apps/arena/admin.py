from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.arena.models import ArenaNPC, HonorReward, MatchReward, RankReward, BuyTimesCost, MatchLogTemplate

class ResourceArenaNPC(resources.ModelResource):
    class Meta:
        model = ArenaNPC

class ResourceHonorReward(resources.ModelResource):
    class Meta:
        model = HonorReward

class ResourceMatchReward(resources.ModelResource):
    class Meta:
        model = MatchReward

class ResourceRankReward(resources.ModelResource):
    class Meta:
        model = RankReward

class ResourceBuyTimesCost(resources.ModelResource):
    class Meta:
        model = BuyTimesCost

class ResourceMatchLogTemplate(resources.ModelResource):
    class Meta:
        model = MatchLogTemplate

@admin.register(ArenaNPC)
class AdminArenaNPC(ImportExportModelAdmin):
    resource_class = ResourceArenaNPC

    list_display = (
        'id', 'npcs'
    )

@admin.register(HonorReward)
class AdminHonorReward(ImportExportModelAdmin):
    resource_class = ResourceHonorReward

    list_display = (
        'id', 'reward', 'des'
    )

@admin.register(MatchReward)
class AdminMatchReward(ImportExportModelAdmin):
    resource_class = ResourceMatchReward

    list_display = (
        'id', 'honor', 'item_id', 'item_amount', 'random_items'
    )

@admin.register(RankReward)
class AdminRankReward(ImportExportModelAdmin):
    resource_class = ResourceRankReward

    list_display = (
        'id', 'reward', 'mail_title', 'mail_content'
    )

@admin.register(BuyTimesCost)
class AdminBuyTimesCost(ImportExportModelAdmin):
    resource_class = ResourceBuyTimesCost

    list_display = ('id', 'diamond')

@admin.register(MatchLogTemplate)
class AdminMatchLogTemplate(ImportExportModelAdmin):
    resource_class = ResourceMatchLogTemplate

    list_display = (
        'id', 'template'
    )