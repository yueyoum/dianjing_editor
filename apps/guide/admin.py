from django.contrib import admin

from apps.guide.models import Guide

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'next_id', 'operate_type', 'operate_target',
        'resume_url'
    )
