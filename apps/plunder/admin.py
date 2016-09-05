from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.plunder.models import (
    BaseStationLevel,
    PlunderIncome,
    PlunderBuyTimesCost,
    PlunderNPC,
)

class ResourceBaseStation(resources.ModelResource):
    class Meta:
        model = BaseStationLevel
        bulk_replace = True

class ResourcePlunderIncome(resources.ModelResource):
    class Meta:
        model = PlunderIncome
        bulk_replace = True

class ResourcePlunderBuyTimesCost(resources.ModelResource):
    class Meta:
        model = PlunderBuyTimesCost
        bulk_replace = True

class ResourcePlunderNPC(resources.ModelResource):
    class Meta:
        model = PlunderNPC
        bulk_replace = True


@admin.register(BaseStationLevel)
class AdminBaseStation(ImportExportModelAdmin):
    resource_class = ResourceBaseStation
    list_display = ('id', 'product', 'exp')

@admin.register(PlunderIncome)
class AdminPlunderInCome(ImportExportModelAdmin):
    resource_class = ResourcePlunderIncome
    list_display = ('id', 'percent', 'exp', 'extra_income')

@admin.register(PlunderBuyTimesCost)
class AdminPlunderBuyTimesCost(ImportExportModelAdmin):
    resource_class = ResourcePlunderBuyTimesCost
    list_display = ('id', 'cost')

@admin.register(PlunderNPC)
class AdminPlunderNPC(ImportExportModelAdmin):
    resource_class = ResourcePlunderNPC
    list_display = ('id', 'level_low', 'level_high', 'way_one', 'way_two', 'way_three')