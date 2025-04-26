from django.contrib.auth.models import BaseUserManager

from rest_framework.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self,phone,password,**extra_fields):
        if not phone:
            raise ValidationError("Phone number is required!")
        if not password:
            raise ValidationError("Password is required!")
        
        extra_fields.setdefault("is_active",True)
        user=self.model(phone=phone,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,phone,password,**extra_fields):
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_staff",True)
        user=self.create_user(phone,password,**extra_fields)
        return user