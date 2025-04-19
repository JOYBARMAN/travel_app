from django.contrib import admin

from core.models import User, UserDetail, Context, DynamicBanner


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["uid", "email", "last_login"]
    fieldsets = (
        (None, {"fields": ("email", "password", "new_password")}),
        (
            "Other",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "phone",
                    "uid",
                    "last_login",
                    "status",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    list_filter = [
        "status",
        "last_login",
    ]
    search_fields = ("phone", "email")
    readonly_fields = ("uid", "last_login")
    list_select_related = True
    show_full_result_count = False
    ordering = ("-created_at",)


@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    model = UserDetail
    list_display = ["uid", "user"]
    fieldsets = (
        (None, {"fields": ("user",)}),
        (
            "Other",
            {
                "fields": (
                    "uid",
                    "bio",
                    "badge",
                    "profile_photo",
                    "contact_number",
                    "contact_email",
                    "location",
                    "address",
                    "facebook_link",
                    "twitter_link",
                    "instagram_link",
                    "linkedin_link",
                    "youtube_link",
                    "website_link",
                    "created_at",
                    "updated_at",
                    "status",
                ),
            },
        ),
    )
    list_filter = [
        "status",
        "created_at",
    ]
    search_fields = ("user__phone", "user__email")
    readonly_fields = ("uid", "created_at", "updated_at")
    list_select_related = True
    show_full_result_count = False
    ordering = ("-created_at",)


@admin.register(Context)
class ContextAdmin(admin.ModelAdmin):
    list_display = ("uid","user", "short_home_banner", "created_at")
    search_fields = ("user__email",)
    readonly_fields = ("created_at", "updated_at")

    def short_home_banner(self, obj):
        return obj.home_banner[:75] + "..." if obj.home_banner else ""

    short_home_banner.short_description = "Home Banner"


@admin.register(DynamicBanner)
class DynamicBannerAdmin(admin.ModelAdmin):
    list_display = ("uid","user", "home", "newsletter", "visited_place", "created_at")
    search_fields = ("user__email",)
    readonly_fields = ("created_at", "updated_at")
