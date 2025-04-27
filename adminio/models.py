from django.db import models
from django.contrib.auth import get_user_model

from accountio.choices import VendorUserRole

from shared.base_model import BaseModel

User = get_user_model()


class AdminUser(BaseModel):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.CharField(
        choices=VendorUserRole.choices, max_length=15, default=VendorUserRole.ADMIN
    )
