# -*- coding: utf-8 -*-

from django.contrib import admin

from apps.training.models import TrainingProperty


@admin.register(TrainingProperty)
class TrainingPropertyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon', 'des', 'minutes', 'tp',
        'cost_type', 'cost_value', 'package', 'order_value',
        'need_building_level',
    )

    list_filter = ('tp',)
