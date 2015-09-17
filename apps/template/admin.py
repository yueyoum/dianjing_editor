from django.contrib import admin

from apps.template.models import SponsorLogTemplate

@admin.register(SponsorLogTemplate)
class SponsorLogTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'template')
