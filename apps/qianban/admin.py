from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.qianban.models import QianBan


class QianBanResource(resources.ModelResource):
    class Meta:
        model = QianBan

@admin.register(QianBan)
class QianBanAdmin(ImportExportModelAdmin):
    resource_class = QianBanResource

    list_display = ('id', 'name', 'des',
                    'condition_tp', 'condition_value',
                    'addition_tp', 'addition_value'
                    )
