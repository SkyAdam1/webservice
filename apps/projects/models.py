from random import randint

from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    EmailField,
    IntegerField,
    TextField,
    URLField,
)
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _


def random_hex() -> str:
    return "#" + str(hex(randint(0, 16777215)))[2:]


class Project(models.Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, db_index=True)
    name = CharField(_("Название проекта"), max_length=150, db_index=True)
    cover = models.ImageField(
        _("Обложка"), upload_to="project_photos/", null=True, blank=True
    )
    site = URLField(_("Ссылка на сайт проекта"), max_length=200)
    description = TextField(_("Описание продукта/сервиса"))
    note = CharField(_("Примечание к проекту"), max_length=150)
    tags = [
        ("Софт Проект", "Софт Проект"),
        ("Программно-аппаратный комплекс", "Программно-аппаратный комплекс"),
    ]
    tag = TextField(_("Тип проекта"), choices=tags, null=True, blank=True)
    responsible = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name="responsible",
        verbose_name=_("Ответственный"),
        db_index=True,
        blank=True,
        null=True,
    )
    umnik = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name="umnik",
        verbose_name=_("Участие в умнике"),
        db_index=True,
        blank=True,
        null=True,
    )

    uss = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name="uss",
        verbose_name=_("Участие в УСС"),
        db_index=True,
        blank=True,
        null=True,
    )

    created_at = DateTimeField(_("Время создания"), auto_now_add=True)
    date = DateField(_("Дата создания"), auto_now_add=True, null=True)
    hex_color = CharField(_("Hex цвет"), max_length=20, blank=True, default="")
    science = IntegerField(_("Наука"), default=0)
    interesting = IntegerField(_("Интересный"), default=0)
    difficult = IntegerField(_("Сложный"), default=0)
    unclear = IntegerField(_("Непонятный"), default=0)
    repeat = IntegerField(_("Повтор"), default=0)
    rating = IntegerField(_("Рейтинг"), default=0)

    def next(self):
        return self.get_next_by_created_at()

    def previous(self):
        return self.get_previous_by_created_at()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(
        self, force_insert=None, force_update=None, using=None, update_fields=None
    ) -> None:
        if not self.hex_color:
            self.hex_color = random_hex()
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    def get_delete_url(self):
        return reverse("project_delete_url", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("project_update_url", kwargs={"pk": self.pk})


class Equipment(models.Model):
    name = CharField(_("Наименование"), max_length=256)
    characteristic = TextField(_("Характеристика"))
    owner = CharField(_("Владелец"), max_length=256)
    contact = CharField(_("Контакт"), max_length=256)
    image = models.ImageField(
        _("Фото"), upload_to="equipment_photos/", null=True, blank=True
    )

    created_at = DateTimeField(_("Дата создания"), auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Criteria(models.Model):
    app = ForeignKey(Project, on_delete=CASCADE, db_index=True)
    expert = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, db_index=True)
    science = BooleanField(_("Есть наука"), default=False)
    interesting = BooleanField(_("Интересный"), default=False)
    difficult = BooleanField(_("Сложный"), default=False)
    unclear = BooleanField(_("Непонятный"), default=False)
    repeat = BooleanField(_("Повтор"), default=False)

    def __str__(self):
        return self.app.name

    def save(
        self, force_insert=None, force_update=None, using=None, update_fields=None
    ) -> None:
        if update_fields:
            self.app.__dict__[update_fields[0]] += (
                1 if self.__dict__[update_fields[0]] else -1
            )
            if update_fields[0] in ["science", "interesting"]:
                self.app.rating += 1 if self.__dict__[update_fields[0]] else -1
            else:
                self.app.rating += -1 if self.__dict__[update_fields[0]] else 1
            self.app.save()
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )


class NiokrUser(models.Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, db_index=True)
    fullname = CharField(_("Фио"), max_length=255)
    phone = CharField(_("Номер телефона"), max_length=255)
    email = EmailField(_("Email"))
    academic_degrees = TextField(_("Ученые степени"), null=True, blank=True)
    academic_titles = TextField(_("Ученые звания"), null=True, blank=True)
    is_responsible = BooleanField(_("Научный руководитель"), default=False)
    ec_id = IntegerField(
        _("ID пользователя в системе эффективного контракта"), blank=True, null=True
    )
    photo = ImageField("Фото", null=True, blank=True)

    def __str__(self):
        return self.fullname


class NiokrProject(models.Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, db_index=True)
    theme = CharField(_("Тема НИОКР"), max_length=150, db_index=True)
    data_project_start = DateField(_("Дата начала исследований (ДД.ММ.ГГГГ)"))
    site = URLField(
        _("Ссылка на сайт проекта (при наличии)"), max_length=200, blank=True, null=True
    )
    base_organisation = CharField(
        _("Базовая организация"), max_length=150, db_index=True
    )
    science_novelty = CharField(_("Научная новизна"), max_length=150, db_index=True)
    commercial_result = CharField(
        _("Коммерческий результат"), max_length=150, db_index=True
    )
    equipment = CharField(
        _("Оборудование, необходимое для реализации проекта"),
        max_length=150,
        db_index=True,
    )
    grants = CharField(_("Наличие грантов"), blank=True, null=True, max_length=2000)
    patents = CharField(_("Наличие патента"), blank=True, null=True, max_length=2000)
    cover = models.ImageField(
        _("Обложка"), upload_to="niokr_project_photos/", null=True, blank=True
    )
    annotation = TextField(_("Аннотация к проекту (до 2000 символов)"), max_length=2000)
    responsible = ForeignKey(NiokrUser, on_delete=CASCADE, related_name="responsible")
    team = ManyToManyField(NiokrUser, blank=True)

    created_at = DateTimeField(_("Время создания"), auto_now_add=True)
    date = DateField(_("Дата создания"), auto_now_add=True, null=True)
    hex_color = CharField(_("Hex цвет"), max_length=20, blank=True, default="")
    science = IntegerField(_("Наука"), default=0)
    interesting = IntegerField(_("Интересный"), default=0)
    difficult = IntegerField(_("Сложный"), default=0)
    unclear = IntegerField(_("Непонятный"), default=0)
    repeat = IntegerField(_("Повтор"), default=0)
    rating = IntegerField(_("Рейтинг"), default=0)

    def next(self):
        return self.get_next_by_created_at()

    def previous(self):
        return self.get_previous_by_created_at()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.theme

    def save(
        self, force_insert=None, force_update=None, using=None, update_fields=None
    ) -> None:
        if not self.hex_color:
            self.hex_color = random_hex()
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    def get_delete_url(self):
        return reverse("niokr_project_delete_url", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("niokr_project_update_url", kwargs={"pk": self.pk})


class NiokrCriteria(models.Model):
    app = ForeignKey(NiokrProject, on_delete=CASCADE, db_index=True)
    expert = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, db_index=True)
    science = BooleanField(_("Есть наука"), default=False)
    interesting = BooleanField(_("Интересный"), default=False)
    difficult = BooleanField(_("Сложный"), default=False)
    unclear = BooleanField(_("Непонятный"), default=False)
    repeat = BooleanField(_("Повтор"), default=False)

    def __str__(self):
        return self.app.theme

    def save(
        self, force_insert=None, force_update=None, using=None, update_fields=None
    ) -> None:
        if update_fields:
            self.app.__dict__[update_fields[0]] += (
                1 if self.__dict__[update_fields[0]] else -1
            )
            if update_fields[0] in ["science", "interesting"]:
                self.app.rating += 1 if self.__dict__[update_fields[0]] else -1
            else:
                self.app.rating += -1 if self.__dict__[update_fields[0]] else 1
            self.app.save()
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
