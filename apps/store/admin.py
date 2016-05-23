from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.store.models import Store, StoreCondition, StoreRefresh

class ResourceStore(resources.ModelResource):
    class Meta:
        model = Store

class ResourceSC(resources.ModelResource):
    class Meta:
        model = StoreCondition

class ResourceSR(resources.ModelResource):
    class Meta:
        model = StoreRefresh



@admin.register(Store)
class AdminStore(ImportExportModelAdmin):
    resource_class = ResourceStore
    list_display = (
        'id', 'tp', 'tp_name', 'club_level_min', 'club_level_max',
        'money_id', 'refresh_hour_interval', 'position',
        'condition_id', 'condition_value',
        'times_limit', 'content',
    )

    list_filter = ('tp',)


@admin.register(StoreCondition)
class AdminSC(ImportExportModelAdmin):
    resource_class = ResourceSC
    list_display = (
        'id', 'des'
    )

@admin.register(StoreRefresh)
class AdminSR(ImportExportModelAdmin):
    resource_class = ResourceSR
    list_display = (
        'id', 'store_tp', 'times', 'diamond'
    )
