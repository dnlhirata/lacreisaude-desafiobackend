from appointments.tests.factories import AppointmentFactory
from django.test import TestCase
from django.urls import reverse

from users.tests.factories import ProfessionalFactory


class ProfessionalViewSetTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.professional = ProfessionalFactory()
        cls.url = reverse("users:professional-list")
        cls.detail_url = reverse("users:professional-detail", kwargs={"pk": cls.professional.id})

    def test_list_professionals(self) -> None:
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_professional(self) -> None:
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.professional.id)

    def test_create_professional(self) -> None:
        name = "John Doe"
        social_name = "John Magu Doe"
        address = "Address Example"
        email = "example@example.com"
        occupation = "Doctor"

        response = self.client.post(
            self.url,
            data={
                "name": name,
                "social_name": social_name,
                "address": address,
                "email": email,
                "occupation": occupation,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], name)
        self.assertEqual(response.data["social_name"], social_name)
        self.assertEqual(response.data["address"], address)
        self.assertEqual(response.data["email"], email)
        self.assertEqual(response.data["occupation"], occupation)

    def test_update_professional(self) -> None:
        name = "George Doe"
        response = self.client.patch(self.detail_url, data={"name": name}, content_type="application/json")

        self.professional.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.professional.id)
        self.assertEqual(response.data["name"], name)
        self.assertEqual(response.data["social_name"], self.professional.user.social_name)

    def test_list_professional_appointments(self) -> None:
        appointment1 = AppointmentFactory(professional=self.professional)
        appointment2 = AppointmentFactory(professional=self.professional)
        other_professional = ProfessionalFactory()
        appointment3 = AppointmentFactory(professional=other_professional)

        url = reverse("users:professional-appointments", kwargs={"pk": self.professional.id})
        response = self.client.get(url)

        appointments = self.professional.appointments.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(appointments.count(), 2)
        self.assertIn(appointment1, appointments)
        self.assertIn(appointment2, appointments)
        self.assertNotIn(appointment3, appointments)
