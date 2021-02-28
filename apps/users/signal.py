from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser


@receiver(post_save, sender=AbstractUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)