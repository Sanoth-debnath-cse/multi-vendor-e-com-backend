from autoslug import AutoSlugField

from django.db import models

from accountio.models import Vendor

from shared.base_model import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    slug = AutoSlugField(
        populate_from="name", unique=True, editable=False, db_index=True
    )
    image = models.ImageField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
