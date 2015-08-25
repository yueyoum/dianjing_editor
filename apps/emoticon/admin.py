from django.contrib import admin

from apps.emoticon.models import Emoticon

@admin.register(Emoticon)
class EmoticonAdmin(admin.ModelAdmin):
    list_display = ('cmd', 'icon')
