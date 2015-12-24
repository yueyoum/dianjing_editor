from django.contrib import admin

from apps.building.models import Building, BuildingLevels, Shop, Sponsor, BusinessBroadcastReward

class BuildingLevelsInline(admin.TabularInline):
    model = BuildingLevels


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'level_up_condition_type', 'des', 'status_des', 'remark',
        'day_effect', 'night_effect',
        'LevelAmount'
    )

    inlines = [BuildingLevelsInline,]

    def LevelAmount(self, obj):
        return obj.levels_info.all().count()

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'unlock_type', 'unlock_value', 'income',
        'mail_title', 'mail_content', 'des',
    )

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon', 'condition', 'total_days',
        'income', 'income_des', 'condition_des',
        'mail_title', 'mail_content',
    )

@admin.register(BusinessBroadcastReward)
class BusinessBroadcastRewardAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'prob')
