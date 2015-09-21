from django.contrib import admin

from apps.activity.models import (
    ActivityCategory,
    Activity,
    ActivitySignIn,
    ActivitySignInDayReward,
    ActivityLoginReward,
)


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'fixed', 'start_at', 'end_at', 'des'
    )


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'category', 'name',
        'des'
    )

    list_filter = ['category', ]


class SignInDayInLine(admin.TabularInline):
    model = ActivitySignInDayReward


@admin.register(ActivitySignIn)
class ActivitySignInAdmin(admin.ModelAdmin):
    list_display = (
        'activity', 'valid_test_divisor', 'valid_test_value',
        'circle_times', 'circle_package',
        'mail_title', 'mail_content'
    )

    inlines = [SignInDayInLine,]


@admin.register(ActivityLoginReward)
class ActivityLoginReward(admin.ModelAdmin):
    list_display = (
        'activity', 'day', 'package'
    )
