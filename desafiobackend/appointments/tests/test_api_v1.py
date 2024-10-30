from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from users.tests.factories import ProfessionalFactory

from appointments.tests.factories import AppointmentFactory


class AppointmentViewSetTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.professional = ProfessionalFactory()
        cls.appointment = AppointmentFactory(professional=cls.professional)
        cls.url = reverse("appointments:appointment-list")
        cls.detail_url = reverse("appointments:appointment-detail", kwargs={"pk": cls.appointment.id})

    def test_list_appointments(self) -> None:
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_appointment(self) -> None:
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.appointment.id)
        self.assertEqual(response.data["professional"], self.professional.id)

    def test_create_appointment(self) -> None:
        date = timezone.now()
        response = self.client.post(self.url, data={"date": date, "professional": self.professional.id})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["date"], date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        self.assertEqual(response.data["professional"], self.professional.id)

    def test_update_appointment(self) -> None:
        professional = ProfessionalFactory()
        response = self.client.patch(
            self.detail_url, data={"professional": professional.id}, content_type="application/json"
        )

        self.appointment.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["date"], self.appointment.date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        self.assertEqual(self.appointment.professional_id, professional.id)
