from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Пользовательский мененджер моделей"""

    def create_user(self, username, email, password, **extra_fields):
        """Создание пользователя"""

        if not email:
            raise ValueError(_("Электронная почта должна быть указана"))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """Создание суперпользователя"""

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_expert", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, email, password, **extra_fields)
