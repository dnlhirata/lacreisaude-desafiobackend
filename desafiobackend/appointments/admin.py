from django.contrib import admin

from appointments.models import Appointment


# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("date", "professional")
    list_filter = ("professional",)
    list_select_related = ("professional",)
    raw_id_fields = ("professional",)
    search_fields = ("professional__name",)
