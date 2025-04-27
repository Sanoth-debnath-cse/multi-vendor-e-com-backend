from django.utils import timezone
from django.db.models import (
    OuterRef,
    Subquery,
    When,
    Value,
    BooleanField,
    Case,
    CharField,
    DateTimeField,
)
from rest_framework.exceptions import NotFound

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAuthenticated

from accountio.models import Vendor, VendorUser

from vendorapi.rest.serializers.vendors import PrivateVendorListSerializer


class PrivateVendorListView(ListAPIView):
    serializer_class = PrivateVendorListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        connected_vendor_ids = VendorUser.objects.filter(user=user).values_list(
            "vendor_id", flat=True
        )

        role_subquery = (
            VendorUser.objects.filter(vendor_id=OuterRef("pk"), user=user)
            .annotate(
                has_last_login=Case(
                    When(last_login__isnull=False, then=Value(True)),
                    default=Value(False),
                    output_field=BooleanField(),
                ),
            )
            .values("last_login", "role", "has_last_login")[:1]
        )

        return (
            Vendor.objects.filter(id__in=connected_vendor_ids, is_active=True)
            .annotate(
                role=Subquery(role_subquery.values("role"), output_field=CharField()),
                last_login=Subquery(
                    role_subquery.values("last_login"), output_field=DateTimeField()
                ),
                has_last_login=Subquery(
                    role_subquery.values("has_last_login"), output_field=BooleanField()
                ),
            )
            .order_by("-has_last_login", "-last_login")
        )


class PrivateVendorDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateVendorListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        vendor_uid = self.kwargs["vendor_uid"]
        user = self.request.user

        try:
            vendor = Vendor.objects.get(uid=vendor_uid, is_active=True)
            vendor_user = VendorUser.objects.filter(vendor=vendor, user=user).first()
            if vendor_user:
                vendor_user.last_login = timezone.now()
                vendor_user.save_dirty_fields()
            return vendor
        except Vendor.DoesNotExist:
            raise NotFound(detail="Vendor not found")

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save_dirty_fields()
