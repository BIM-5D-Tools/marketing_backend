from django.contrib import admin
from .models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "company", "created_at")
    readonly_fields = (
        "full_name",
        "email",
        "phone",
        "company",
        "message",
        "created_at",
    )
