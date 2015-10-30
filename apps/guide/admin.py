from django.contrib import admin

from apps.guide.models import Guide, GuideDialogAfter, GuideDialogBefore

class GuideDialogBeforeInLine(admin.TabularInline):
    model = GuideDialogBefore

class GuideDialogAfterInLine(admin.TabularInline):
    model = GuideDialogAfter



@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'next_id', 'operate_type', 'operate_target',
        'resume_url', 'arrow', 'picture', 'position', 'package',
    )

    inlines = [GuideDialogBeforeInLine, GuideDialogAfterInLine]
