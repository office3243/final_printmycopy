from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from .validators import phone_number_validator
# from wallets.models import Wallet
from django.db.models.signals import post_save


class User(AbstractBaseUser, PermissionsMixin):

    phone = models.CharField(max_length=13, validators=[phone_number_validator, MaxLengthValidator(limit_value=13),
                                                        MinLengthValidator(limit_value=13)], unique=True)
    email = models.EmailField(blank=True, null=True)
    phone_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True, default="Pune")
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.get_display_text

    @property
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name).strip()

    @property
    def get_display_text(self):
        return self.get_full_name or self.phone

    @property
    def get_short_name(self):
        return self.first_name or self.phone

    def make_phone_verified_and_active(self):
        self.is_active = True
        self.phone_verified = True
        self.save()

