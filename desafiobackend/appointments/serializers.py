from rest_framework.serializers import ModelSerializer

from appointments.models import Appointment


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            "id",
            "date",
            "professional",
        )
