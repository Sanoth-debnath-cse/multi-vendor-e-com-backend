from django.db.models import Manager


class CustomVendorManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
