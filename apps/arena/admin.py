from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.arena.models import ArenaNPC, HonorReward, MatchReward, RankReward, BuyTimesCost, MatchLogTemplate, \
    SearchRange, ResetCost, RankRewardWeekly


class ResourceArenaNPC(resources.ModelResource):
    class Meta:
        model = ArenaNPC
        bulk_replace = True


class ResourceHonorReward(resources.ModelResource):
    class Meta:
        model = HonorReward
        bulk_replace = True


class ResourceMatchReward(resources.ModelResource):
    class Meta:
        model = MatchReward
        bulk_replace = True


class ResourceRankReward(resources.ModelResource):
    class Meta:
        model = RankReward
        bulk_replace = True


class ResourceBuyTimesCost(resources.ModelResource):
    class Meta:
        model = BuyTimesCost
        bulk_replace = True


class ResourceMatchLogTemplate(resources.ModelResource):
    class Meta:
        model = MatchLogTemplate
        bulk_replace = True


class ResourceSearchRange(resources.ModelResource):
    class Meta:
        model = SearchRange
        bulk_replace = True


class ResourceResetCost(resources.ModelResource):
    class Meta:
        model = ResetCost
        bulk_replace = True

class ResourceRankRewardWeekly(resources.ModelResource):
    class Meta:
        model = RankRewardWeekly
        bulk_replace = True


@admin.register(ArenaNPC)
class AdminArenaNPC(ImportExportModelAdmin):
    resource_class = ResourceArenaNPC

    list_display = (
        'id', 'score_low', 'score_high', 'npcs', 'amount'
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
        'id', 'rank_des', 'reward', 'mail_title', 'mail_content'
    )

@admin.register(RankRewardWeekly)
class AdminRankReward(ImportExportModelAdmin):
    resource_class = ResourceRankRewardWeekly

    list_display = (
        'id', 'rank_des', 'reward', 'mail_title', 'mail_content'
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


@admin.register(SearchRange)
class AdminSearchRange(ImportExportModelAdmin):
    resource_class = ResourceSearchRange
    list_display = ('id', 'range_1', 'range_2', 'score_win', 'score_lose')


@admin.register(ResetCost)
class AdminResetCost(ImportExportModelAdmin):
    resource_class = ResourceResetCost
    list_display = ('id', 'diamond')
