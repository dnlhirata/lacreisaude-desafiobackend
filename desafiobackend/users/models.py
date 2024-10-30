from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import EmailField
from django.db.models import Model
from django.db.models import OneToOneField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class User(AbstractUser):
    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), max_length=255)
    social_name = CharField(_("Social Name of User"), blank=True, max_length=255)
    address = CharField(_("Address"), max_length=255)
    first_name = None
    last_name = None
    email = EmailField(_("email address"), unique=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()


class Professional(Model):
    occupation = CharField(_("Occupation"), max_length=255)
    user = OneToOneField(User, on_delete=CASCADE)

    class Meta:
        verbose_name = _("Professional")
        verbose_name_plural = _("Professionals")

    def __str__(self: "Professional") -> str:
        return self.user.name
