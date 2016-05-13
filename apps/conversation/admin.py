from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.conversation.models import Conversation, ConversationInfo, ChallengeConversation


class ConversationInLine(admin.TabularInline):
    model = ConversationInfo


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'tp', 'condition_value', 'is_loop', 'time_tp'
    )

    inlines = [ConversationInLine]


class ResourceCC(resources.ModelResource):
    class Meta:
        model = ChallengeConversation

@admin.register(ChallengeConversation)
class AdminCC(ImportExportModelAdmin):
    resource_class = ResourceCC
    list_display = (
        'id', 'challenge_id', 'mode', 'pos',
        'picture', 'content'
    )