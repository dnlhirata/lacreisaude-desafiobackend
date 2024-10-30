from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.models import Professional
from users.models import User
from users.serializers import ProfessionalSerializer


class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

    def perform_create(self, serializer: "ProfessionalSerializer") -> None:
        user_data = serializer.validated_data.pop("user")
        ocuppation = serializer.validated_data.pop("occupation")
        user = User.objects.create_user(
            **user_data,
        )
        serializer.save(user=user, occupation=ocuppation)

    @action(detail=True, methods=["get"], serializer_class=AppointmentSerializer)
    def appointments(self, request: Request, pk: int = None) -> list[Appointment]:
        professional = self.get_object()
        appointments = professional.appointments.all()
        serializer = self.get_serializer(appointments, many=True)

        return Response(serializer.data)
