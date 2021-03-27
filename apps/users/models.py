from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField, EmailField
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = EmailField(
        ("E-mail"),
        unique=True,
        error_messages={"unique": _("Такой email уже зарегистрирован")},
    )
    is_expert = BooleanField(_("Отметьте, если являетесь экспертом"), default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
