from django.contrib import admin
from apps.task.models import (
    TaskCondition,
    TaskMain,
    TaskDaily,
)

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ResourceTC(resources.ModelResource):
    class Meta:
        model = TaskCondition
        bulk_replace = True


class ResourceTaskMain(resources.ModelResource):
    class Meta:
        model = TaskMain
        bulk_replace = True


class ResourceTaskDaily(resources.ModelResource):
    class Meta:
        model = TaskDaily
        bulk_replace = True


@admin.register(TaskCondition)
class AdminTC(ImportExportModelAdmin):
    resource_class = ResourceTC
    list_display = ('id', 'name', 'param', 'ui', 'server_module')


@admin.register(TaskMain)
class AdminTaskMain(ImportExportModelAdmin):
    resource_class = ResourceTaskMain
    list_display = ('id', 'name', 'des', 'challenge_id', 'items')


@admin.register(TaskDaily)
class AdminTaskDaily(ImportExportModelAdmin):
    resource_class = ResourceTaskDaily
    list_display = ('id', 'name', 'des', 'club_level', 'vip_level',
                    'condition_id', 'condition_value',
                    'rewards',
                    )
