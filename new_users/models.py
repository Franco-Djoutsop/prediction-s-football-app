from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustumUserManager

#|__________________________________________________________________________________________|
#|  creation du model personnaliser , ou les informations de connexion seront enregistre    |
#|__________________________________________________________________________________________|

class Bettor(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'),unique=True)
    number = models.CharField(max_length=100,unique=True)
    
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['number',]

    objects = CustumUserManager()
    
    def __str__(self):
        return self.email