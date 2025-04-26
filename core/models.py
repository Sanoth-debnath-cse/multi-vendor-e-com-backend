from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from shared.base_model import BaseModel
from .managers import CustomUserManager


# Create your models here.
class User(AbstractBaseUser,PermissionsMixin,BaseModel):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email=models.EmailField(blank=True,null=True)
    phone=PhoneNumberField(unique=True,db_index=True)
    is_active=models.BooleanField(default=True)
    is_varified=models.BooleanField(default=True)
    image=models.ImageField(blank=True,null=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD ="phone"
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()

