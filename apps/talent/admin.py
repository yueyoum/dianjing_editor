from django.contrib import admin

from apps.talent.models import Talent

# Register your models here.


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = [
            "id", "tp", "position", "name", "des",
            "image", "unlock", "up_need", "effect_id",
        ]
