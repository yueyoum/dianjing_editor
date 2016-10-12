from django.contrib import admin

from apps.errormsg.models import ErrorMsg

@admin.register(ErrorMsg)
class ErrorMsgAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'error_index', 'text_zh', 'is_retry', 'jump_to', 'des'
    )
