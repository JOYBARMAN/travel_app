from django.contrib import admin
from .models import Post, UserGallery


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("uid", "title", "user", "post_type", "created_at")
    search_fields = ("title", "user__email", "post_type")
    list_filter = ("post_type", "created_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(UserGallery)
class UserGalleryAdmin(admin.ModelAdmin):
    list_display = ("uid", "title", "user", "country", "created_at")
    search_fields = ("title", "user__email", "country")
    list_filter = ("country", "created_at")
    readonly_fields = ("created_at", "updated_at")
