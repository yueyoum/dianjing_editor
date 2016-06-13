
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
        bulk_replace = True



@admin.register(TowerSaleGoods)
class TowerSaleGoodsAdmin(ImportExportModelAdmin):
    resource_class = ResourceTowerSaleGoods

    list_display = (
            "id", "price_original", "price_now", "vip_need", "item_id", "amount", "des",
    )


class ResourceTowerStarReward(resources.ModelResource):
    class Meta:
        model = TowerStarReward
        bulk_replace = True



@admin.register(TowerStarReward)
class TowerStarRewardAdmin(ImportExportModelAdmin):
    resource_class = ResourceTowerStarReward

    list_display = (
            "id", "reward",
    )


class ResourceTowerRankReward(resources.ModelResource):
    class Meta:
        model = TowerRankReward
        bulk_replace = True



@admin.register(TowerRankReward)
class TowerRankRewardAdmin(ImportExportModelAdmin):
    resource_class = ResourceTowerRankReward

    list_display = (
            "id", 'rank_des', "reward", "mail_title", "mail_content",
    )


class ResourceTowerGameLevel(resources.ModelResource):
    class Meta:
        model = TowerGameLevel
        bulk_replace = True



@admin.register(TowerGameLevel)
class TowerGameLevelAdmin(ImportExportModelAdmin):
    resource_class = ResourceTowerGameLevel

    list_display = (
            "id", "name", "talent_id", "staffs",
    )


class ResourceTowerResetCost(resources.ModelResource):
    class Meta:
        model = TowerResetCost
        bulk_replace = True



@admin.register(TowerResetCost)
class TowerResetCostAdmin(ImportExportModelAdmin):
    resource_class = ResourceTowerResetCost

    list_display = (
        "id", "cost",
    )
