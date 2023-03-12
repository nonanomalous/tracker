# from https://testdriven.io/blog/django-custom-user-model/

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager, StaffManager

class ContextMethodMixin:
    def is_support_agent(self):
        return self.groups.exclude(name="Student").exists()

    def main_cols(self):
        if self.is_superuser:
            return 10
        else:
            return 12

class User(AbstractBaseUser, PermissionsMixin, ContextMethodMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=32, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    active_view = models.CharField(max_length=32, default="Open")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    staff = StaffManager()

    def __str__(self):
        return self.email
