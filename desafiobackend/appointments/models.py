from typing import ClassVar

from django.db.models import CASCADE
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import UniqueConstraint
from django_extensions.db.models import TimeStampedModel


class Appointment(TimeStampedModel):
    """Appointment model representing a scheduled appointment with a professional.

    Attributes:
        professional (ForeignKey): A foreign key to the Professional model.
        date (DateTimeField): The date and time of the appointment.

    Meta:
        verbose_name (str): The human-readable name of the model.
        verbose_name_plural (str): The human-readable plural name of the model.
        constraints (list): A list of constraints for the model, ensuring that each professional can only have one appointment at a specific date and time.

    Methods:
        __str__(): Returns a string representation of the appointment, including the date and the professional.

    """

    professional = ForeignKey("users.Professional", on_delete=CASCADE)
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
