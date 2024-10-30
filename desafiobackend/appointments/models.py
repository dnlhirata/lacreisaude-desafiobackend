from typing import ClassVar

from django.db.models import CASCADE
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import UniqueConstraint
from django_extensions.db.models import TimeStampedModel


class Appointment(TimeStampedModel):
    professional = ForeignKey("users.Professional", on_delete=CASCADE, related_name="appointments")
    date = DateTimeField()

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
        constraints: ClassVar = [
            UniqueConstraint(
                fields=["professional", "date"],
                name="unique_professional_date",
            )
        ]

    def __str__(self: "Appointment") -> str:
        return f"{self.date} - {self.professional}"
