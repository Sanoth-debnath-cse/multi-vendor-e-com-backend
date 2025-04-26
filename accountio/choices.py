from django.db import models


class VendorUserRole(models.TextChoices):
    OWNER = "OWNER", "Owner"
    ADMIN = "ADMIN", "Admin"
    STAFF = "STAFF", "Staff"
