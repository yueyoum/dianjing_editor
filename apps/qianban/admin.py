from django.contrib import admin

from apps.qianban.models import QianBan

@admin.register(QianBan)
class QianBanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'des')
