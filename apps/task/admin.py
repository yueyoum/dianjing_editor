from django.contrib import admin
from apps.task.models import (
    TaskType,
    Task,
    TaskStatus,
    TaskTrigger,
    TaskTargetType,
    TaskTarget,
    RandomEvent,
    RandomEventDialogAfter,
    RandomEventDialogBefore,
)


# Register your models here.
class TaskTargetInLine(admin.TabularInline):
    model = TaskTarget


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'next_task', 'trigger_tp',
                    'trigger_rate', 'tp', 'reward',
                    'client_task', 'success_rate',
                    )
    inlines = [TaskTargetInLine, ]


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(TaskTrigger)
class TaskTriggerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(TaskTargetType)
class TaskTargetTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class EventDialogBeforeInLine(admin.TabularInline):
    model = RandomEventDialogBefore


class EventDialogAfterInLine(admin.TabularInline):
    model = RandomEventDialogAfter


@admin.register(RandomEvent)
class RandomEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'level_min', 'level_max', 'trig_name', 'package')
    inlines = [EventDialogBeforeInLine, EventDialogAfterInLine]
