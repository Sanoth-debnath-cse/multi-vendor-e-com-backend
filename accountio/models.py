from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.contrib.auth import get_user_model

from accountio.choices import VendorUserRole

from shared.base_model import BaseModel

User = get_user_model()


class Vendor(BaseModel):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True)
    logo = models.ImageField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    contact_number = PhoneNumberField(blank=True, null=True)
    website_url = models.URLField(blank=True)
    address = models.CharField(blank=True, null=True, max_length=255)


class VendorUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    role = models.CharField(
        choices=VendorUserRole.choices, max_length=15, default=VendorUserRole.STAFF
    )
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ("user", "vendor")
