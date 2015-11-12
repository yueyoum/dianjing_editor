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
    list_display = ('id', 'name', 'des', 'next_task', 'trigger',
                    'trigger_value', 'tp', 'reward',
                    'client_task', 'success_rate',
                    'task_begin',
                    )
    inlines = [TaskTargetInLine, ]


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'des')


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(TaskTrigger)
class TaskTriggerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(TaskTargetType)
class TaskTargetTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mode', 'type_category', 'des')


class EventDialogBeforeInLine(admin.TabularInline):
    model = RandomEventDialogBefore


class EventDialogAfterInLine(admin.TabularInline):
    model = RandomEventDialogAfter


@admin.register(RandomEvent)
class RandomEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'target', 'name', 'icon', 'level_min', 'level_max', 'trig_name', 'package')
    inlines = [EventDialogBeforeInLine, EventDialogAfterInLine]
