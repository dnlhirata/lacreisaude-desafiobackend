from django.contrib import admin
from users.models import Professional


# Register your models here.
@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ("user__name", "user__social_name", "user__email", "occupation")
    list_filter = ("occupation",)
    search_fields = ("user__name", "user__social_name", "user__email")
