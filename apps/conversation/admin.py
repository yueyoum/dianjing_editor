from django.contrib import admin

# Register your models here.

from apps.conversation.models import Conversation, ConversationInfo


class ConversationInLine(admin.TabularInline):
    model = ConversationInfo


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'tp', 'condition_value', 'is_loop', 'time_tp', 'conversation'
    )

    inlines = [ConversationInLine]
