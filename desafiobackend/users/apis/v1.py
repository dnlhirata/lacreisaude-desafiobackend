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
