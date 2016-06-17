from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.qianban.models import QianBan


class QianBanResource(resources.ModelResource):
    class Meta:
        model = QianBan
        bulk_replace = True

@admin.register(QianBan)
class QianBanAdmin(ImportExportModelAdmin):
    resource_class = QianBanResource

    list_display = ('id', 'staff_oid', 'name', 'des', 'story_des',
                    'condition_tp', 'condition_value',
                    'talent_effect_id'
                    )
