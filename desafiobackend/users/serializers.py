from rest_framework.serializers import CharField
from rest_framework.serializers import EmailField
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ReadOnlyField

from users.models import Professional


class ProfessionalSerializer(ModelSerializer):
    user_id = ReadOnlyField(source="user.id")
    name = CharField(source="user.name", max_length=255)
    social_name = CharField(source="user.social_name", max_length=255, required=False)
    address = CharField(source="user.address")
    email = EmailField(source="user.email")

    class Meta:
        model = Professional
        fields = (
            "user_id",
            "name",
            "social_name",
            "address",
            "email",
            "occupation",
        )

    def update(self, instance: Professional, validated_data: dict) -> Professional:
        user_data = validated_data.pop("user")
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)

        instance.user.save()

        return super().update(instance, validated_data)
