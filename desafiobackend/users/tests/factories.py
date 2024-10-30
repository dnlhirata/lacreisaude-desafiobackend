from factory import Faker
from factory import SubFactory
from factory.django import DjangoModelFactory

from users.models import Professional
from users.models import User


class UserFactory(DjangoModelFactory):
    name = Faker("name")
    email = Faker("email")
    address = Faker("address")

    class Meta:
        model = User


class ProfessionalFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    occupation = Faker("word")

    class Meta:
        model = Professional
