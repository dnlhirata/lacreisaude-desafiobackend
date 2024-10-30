from django.contrib import admin

from users.models import Professional
from users.models import User


class ProfessionalInline(admin.StackedInline):
    model = Professional
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (ProfessionalInline,)
    list_display = ("name",)
