from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.purchase.models import PurchaseGoods,PurchaseYueka, PurchaseFirstReward

class ResourceGoods(resources.ModelResource):
    class Meta:
        model = PurchaseGoods
        bulk_replace = True

class ResourceYueka(resources.ModelResource):
    class Meta:
        model = PurchaseYueka
        bulk_replace = True

class ResourceFirstReward(resources.ModelResource):
    class Meta:
        model = PurchaseFirstReward
        bulk_replace = True

@admin.register(PurchaseGoods)
class AdminGoods(ImportExportModelAdmin):
    resource_class = ResourceGoods
    list_display = (
        'id', 'des', 'rmb', 'vip_exp', 'diamond', 'diamond_extra'
    )

@admin.register(PurchaseYueka)
class AdminYueka(ImportExportModelAdmin):
    resource_class = ResourceYueka
    list_display = (
        'id', 'des', 'rmb', 'vip_exp', 'rewards', 'mail_title', 'mail_content'
    )

@admin.register(PurchaseFirstReward)
class AdminFirstReward(ImportExportModelAdmin):
    resource_class = ResourceFirstReward
    list_display = ('id', 'rewards')