from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField


class User(AbstractBaseUser, PermissionsMixin):
    slug = AutoSlugField(populate_from='username')
    email = models.EmailField(verbose_name=_("Email"), unique=True)
    username = models.CharField(verbose_name=_("Username"), max_length=40, unique=True)
    first_name = models.CharField(verbose_name=_("First name"), max_length=40, blank=True, null=True)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=40, blank=True, null=True)
    dob = models.DateField(verbose_name=_("Date of birth (YYYY-MM-DD)"), blank=True, null=True)
    age = models.IntegerField(verbose_name=_("Age"), blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name_plural = _("Users")
        verbose_name = _("User")

    def __str__(self):
        return f"{self.username}"

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
