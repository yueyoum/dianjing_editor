from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.qianban.models import QianBan, Inspire, InspireLevelAddition, InspireStepAddition


class QianBanResource(resources.ModelResource):
    class Meta:
        model = QianBan
        bulk_replace = True

class ResourceInspire(resources.ModelResource):
    class Meta:
        model = Inspire
        bulk_replace = True

class ResourceInspireLA(resources.ModelResource):
    class Meta:
        model = InspireLevelAddition
        bulk_replace = True

class ResourceInspireSA(resources.ModelResource):
    class Meta:
        model = InspireStepAddition
        bulk_replace = True

@admin.register(QianBan)
class QianBanAdmin(ImportExportModelAdmin):
    resource_class = QianBanResource

    list_display = ('id', 'staff_oid', 'name', 'des', 'story_des',
                    'condition_tp', 'condition_value',
                    'talent_effect_id'
                    )

@admin.register(Inspire)
class AdminInspire(ImportExportModelAdmin):
    resource_class = ResourceInspire
    list_display = ('id', 'challenge_id', 'des')
    ordering = ('id',)

@admin.register(InspireLevelAddition)
class AdminInspireLA(ImportExportModelAdmin):
    resource_class = ResourceInspireLA
    list_display = ('id', 'des')
    ordering = ('id',)

@admin.register(InspireStepAddition)
class AdminInspireSA(ImportExportModelAdmin):
    resource_class = ResourceInspireSA
    list_display = ('id', 'des')
    ordering = ('id',)