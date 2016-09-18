from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.party.models import PartyBuyItem, PartyLevel, PartyMessageTemplate

class ResourcePL(resources.ModelResource):
    class Meta:
        model = PartyLevel
        bulk_replace = True

class ResourcePBI(resources.ModelResource):
    class Meta:
        model = PartyBuyItem
        bulk_replace = True

class ResourcePMT(resources.ModelResource):
    class Meta:
        model = PartyMessageTemplate
        bulk_replace = True

@admin.register(PartyLevel)
class AdminPL(ImportExportModelAdmin):
    resource_class = ResourcePL
    list_display = (
        'id', 'name', 'need_union_level', 'need_diamond',
        'talent_skills', 'item_id', 'buy_one', 'buy_two',
    )

@admin.register(PartyBuyItem)
class AdminPBI(ImportExportModelAdmin):
    resource_class = ResourcePBI
    list_display = (
        'id', 'name', 'cost', 'reward',
    )

@admin.register(PartyMessageTemplate)
class AdminPMT(ImportExportModelAdmin):
    resource_class = ResourcePMT
    list_display = ('id', 'template')