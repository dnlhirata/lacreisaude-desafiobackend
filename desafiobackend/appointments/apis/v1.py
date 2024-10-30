from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer
from rest_framework.viewsets import ModelViewSet


class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
