from django.contrib import admin

from apps.welfare.models import (
    WelfareLevelReward,
    WelfareNewPlayer,
    WelfareSignIn,
)

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ResourceSignIn(resources.ModelResource):
    class Meta:
        model = WelfareSignIn
        bulk_replace = True

class ResourceNewPlayer(resources.ModelResource):
    class Meta:
        model = WelfareNewPlayer
        bulk_replace = True

class ResourceLevelReward(resources.ModelResource):
    class Meta:
        model = WelfareLevelReward
        bulk_replace = True



@admin.register(WelfareSignIn)
class AdminSignIn(ImportExportModelAdmin):
    resource_class = ResourceSignIn
    list_display = ('id', 'name', 'reward', 'vip', 'vip_name', 'vip_reward')

@admin.register(WelfareNewPlayer)
class AdminNewPlayer(ImportExportModelAdmin):
    resource_class = ResourceNewPlayer
    list_display = ('id', 'name', 'day', 'reward')

@admin.register(WelfareLevelReward)
class AdminLevelReward(ImportExportModelAdmin):
    resource_class = ResourceLevelReward
    list_display = ('id', 'name', 'level', 'reward')