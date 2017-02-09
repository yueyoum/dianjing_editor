from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.conversation.models import  ChallengeConversation


class ResourceCC(resources.ModelResource):
    class Meta:
        model = ChallengeConversation

@admin.register(ChallengeConversation)
class AdminCC(ImportExportModelAdmin):
    resource_class = ResourceCC
    list_display = (
        'id', 'challenge_id', 'mode', 'position',
        'icon', 'dialog'
    )
