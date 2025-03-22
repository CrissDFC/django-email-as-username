# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager  # Lo crearemos en el siguiente paso

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True, max_length=255)
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("staff"), default=False)  # Necesario para acceder al admin

    # Campos adicionales (personaliza según tus necesidades)
    phone = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = "email"  # Campo usado para autenticación (reemplaza al username)
    REQUIRED_FIELDS = ["first_name", "last_name"]  # Campos obligatorios al crear usuario

    objects = CustomUserManager()  # Manager personalizado

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email


