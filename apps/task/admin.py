from django.contrib import admin
from apps.task.models import (
    RandomEvent,
    RandomEventDialogAfter,
    RandomEventDialogBefore,

    TaskCondition,
    TaskMain,
    TaskDaily,
)

from import_export import resources
from import_export.admin import ImportExportModelAdmin



class EventDialogBeforeInLine(admin.TabularInline):
    model = RandomEventDialogBefore


class EventDialogAfterInLine(admin.TabularInline):
    model = RandomEventDialogAfter


@admin.register(RandomEvent)
class RandomEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'level_min', 'level_max', 'trig_name', 'package')
    inlines = [EventDialogBeforeInLine, EventDialogAfterInLine]


class ResourceTC(resources.ModelResource):
    class Meta:
        model = TaskCondition

class ResourceTaskMain(resources.ModelResource):
    class Meta:
        model = TaskMain

class ResourceTaskDaily(resources.ModelResource):
    class Meta:
        model = TaskDaily


@admin.register(TaskCondition)
class AdminTC(ImportExportModelAdmin):
    resource_class = ResourceTC
    list_display = ('id', 'name', 'ui')


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