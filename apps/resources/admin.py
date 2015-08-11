from django.contrib import admin

from apps.resources.models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon'
    )
