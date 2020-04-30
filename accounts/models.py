from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True,
    )
    display_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["display_name"]

    def __str__(self):
        return self.display_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
