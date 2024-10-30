from factory import Faker
from factory import SubFactory
from factory.django import DjangoModelFactory
from users.tests.factories import ProfessionalFactory

from appointments.models import Appointment


class AppointmentFactory(DjangoModelFactory):
    date = Faker("date_time")
    professional = SubFactory(ProfessionalFactory)

    class Meta:
        model = Appointment
