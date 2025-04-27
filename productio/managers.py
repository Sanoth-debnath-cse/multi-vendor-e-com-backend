from django.db.models import Manager


class CustomProductManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
