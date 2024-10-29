from django.contrib import admin

from users.models import Professional


# Register your models here.
@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ("name", "social_name", "email", "occupation")
    list_filter = ("occupation",)
    search_fields = ("name", "social_name", "email")
