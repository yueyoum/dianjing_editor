from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.activity.models import (
    NewPlayerActivity,
    DailyBuy,
    OnlineTimeActivity,
    ChallengeActivity,
    PurchaseContinuesActivity,
    LevelGrowingActivity,
)

class ResourceNewPlayer(resources.ModelResource):
    class Meta:
        model = NewPlayerActivity
        bulk_replace = True

class ResourceDailyBuy(resources.ModelResource):
    class Meta:
        model = DailyBuy
        bulk_replace = True

class ResourceOTA(resources.ModelResource):
    class Meta:
        model = OnlineTimeActivity
        bulk_replace = True

class ResourceCA(resources.ModelResource):
    class Meta:
        model = ChallengeActivity
        bulk_replace = True

class ResourcePCA(resources.ModelResource):
    class Meta:
        model = PurchaseContinuesActivity
        bulk_replace = True

class ResourceLGA(resources.ModelResource):
    class Meta:
        model = LevelGrowingActivity
        bulk_replace = True


@admin.register(NewPlayerActivity)
class AdminNewPlayer(ImportExportModelAdmin):
    resource_class = ResourceNewPlayer
    list_display = (
        'id', 'day', 'name',
        'condition_id', 'condition_value',
        'rewards', 'show_progress'
    )

@admin.register(DailyBuy)
class AdminDailyBuy(ImportExportModelAdmin):
    resource_class = ResourceDailyBuy
    list_display = (
        'id', 'items', 'diamond_original', 'diamond_now'
    )

@admin.register(OnlineTimeActivity)
class AdminOTA(ImportExportModelAdmin):
    resource_class = ResourceOTA
    list_display = (
        'id', 'online_time', 'des', 'rewards'
    )

@admin.register(ChallengeActivity)
class AdminCA(ImportExportModelAdmin):
    resource_class = ResourceCA
    list_display = ('id', 'des', 'rewards')

@admin.register(PurchaseContinuesActivity)
class AdminPCA(ImportExportModelAdmin):
    resource_class = ResourcePCA
    list_display = ('id', 'des', 'rewards')

@admin.register(LevelGrowingActivity)
class AdminLGA(ImportExportModelAdmin):
    resource_class = ResourceLGA
    list_display = ('id', 'des', 'rewards')
