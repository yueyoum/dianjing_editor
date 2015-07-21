from django.contrib import admin
from apps.task.models import TaskType, Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'des', 'tp', 'num', 'reward')

@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'des')
