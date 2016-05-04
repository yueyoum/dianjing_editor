
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.training_tower.models import (
    TowerSaleGoods,
    TowerStarReward,
    TowerRankReward,
    TowerGameLevel,
    TowerResetCost,
)

# Register your models here.


class ResourceTowerSaleGoods(resources.ModelResource):
    class Meta:
        model = TowerSaleGoods


@admin.register(TowerSaleGoods)
class TowerSaleGoodsAdmin(ImportExportModelAdmin):
    resource_class = ResourceTowerSaleGoods

    list_display = (
            "id", "item", "price", "sale", "vip_need", "num", "des",
    )


class ResourceTowerStarReward(resources.ModelResource):
    class Meta:
        model = TowerStarReward


@admin.register(TowerStarReward)
class TowerStarRewardAdmin(ImportExportModelAdmin):
    resource_class = ResourceTowerStarReward

    list_display = (
            "id", "reward", "star",
    )


class ResourceTowerRankReward(resources.ModelResource):
    class Meta:
        model = TowerRankReward


@admin.register(TowerRankReward)
class TowerRankRewardAdmin(ImportExportModelAdmin):
    resource_class = ResourceTowerRankReward

    list_display = (
            "id", "reward", "rank_cap", "rank_floor", "mail_sender",
    )


class ResourceTowerGameLevel(resources.ModelResource):
    class Meta:
        model = TowerGameLevel


@admin.register(TowerGameLevel)
class TowerGameLevelAdmin(ImportExportModelAdmin):
    resource_class = ResourceTowerGameLevel

    list_display = (
            "id", "name", "buff", "npc_path", "star_one", "star_two", "star_three",
            "sale_goods", "roulette_three", "roulette_six", "roulette_nine",
    )


class ResourceTowerResetCost(resources.ModelResource):
    class Meta:
        model = TowerResetCost


@admin.register(TowerResetCost)
class TowerResetCostAdmin(ImportExportModelAdmin):
    resource_class = ResourceTowerResetCost

    list_display = (
        "id", "cost",
    )