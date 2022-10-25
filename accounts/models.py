from enum import unique
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

from django.contrib.auth.models import User

ROLES = [
    ("developer", "Developer"),
    ("designer", "Designer")
]

# Create your models here.


class AccountManager(BaseUserManager):

    def create_user(self, email, name, role, date_of_birth=None, password=None):
        if not email:
            raise ValueError("Email is required")
        if not name:
            raise ValueError("Name is required")
        if not role:
            raise ValueError("Role is required")

        user = self.model(name=name, email=email, role=role,
                          date_of_birth=date_of_birth)

        user.set_password(password)
        user.save(self._db)

        return user

    def create_superuser(self, email, name, role, date_of_birth=None, password=None):
        user = self.create_user(
            email=email, name=name, date_of_birth=date_of_birth, password=password, role=role)

        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=100, choices=ROLES)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name', 'role']

    objects = AccountManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'accounts'
