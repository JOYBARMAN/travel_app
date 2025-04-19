from django.contrib import admin
from .models import Newsletter, Contact


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("uid","email", "user", "created_at")
    search_fields = ("email", "user__email")
    list_filter = ("created_at",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("uid","email", "first_name", "last_name", "subject", "created_at")
    search_fields = ("email", "first_name", "last_name", "subject", "user__email")
    list_filter = ("created_at",)
