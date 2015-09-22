from django.contrib import admin

from apps.client_npc.models import ClientNPC, ClientNPCDiaLog

class DiaLogInLine(admin.TabularInline):
    model = ClientNPCDiaLog

@admin.register(ClientNPC)
class ClientNPCAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'model', 'position',
        'function', 'value'
    )

    inlines = [DiaLogInLine, ]

