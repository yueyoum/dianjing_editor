# -*- coding: utf-8 -*-

# from django.contrib import admin
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
#
# from apps.package.models import Package
#
# class PackageResource(resources.ModelResource):
#     class Meta:
#         model = Package
#
# @admin.register(Package)
# class PackageAdmin(ImportExportModelAdmin):
#     resource_class = PackageResource
#
#     list_display = (
#         'id', 'name', 'tp',  'des',
#     )
#
#     search_fields = ('name',)
#     list_filter = ('tp',)
#
#     fieldsets = (
#         (None, {
#             'fields': ('id', 'name', 'tp', 'des')
#         }),
#
#         ('属性包', {
#             'classes': ('collapse',),
#             'fields': ('attr_mode', 'attr_random_amount', 'attr_random_value',
#                        'caozuo', 'baobing', 'jingying', 'zhanshu',
#                        'biaoyan', 'yingxiao', 'zhimingdu',
#                        'staff_exp',
#                        ),
#         }),
#
#         ('物品包', {
#             'classes': ('collapse',),
#             'fields': ('item_mode', 'item_random_amount',
#                        'gold', 'diamond', 'club_renown',
#                        'items', 'staff_cards',
#                        ),
#         }),
#     )
