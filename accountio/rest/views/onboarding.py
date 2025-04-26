from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from accountio.models import Vendor
from accountio.rest.serializers.onboarding import (
    PublicUserOnboardingSerializer,
    PublicVendorOnboardingSerializer,
    PublicVendorMiniSerializer,
)

User = get_user_model()


class PublicUserOnboardingView(ListCreateAPIView):
    serializer_class = PublicUserOnboardingSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.filter(is_active=True)


class PublicVendorOnboardingView(ListCreateAPIView):
    serializer_class = PublicVendorOnboardingSerializer
    permission_classes = [AllowAny]
    queryset = Vendor.objects.filter(is_active=True)


class PublicVendorDetailsView(RetrieveAPIView):
    serializer_class = PublicVendorMiniSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        vendor_slug = self.kwargs.get("vendor_slug")

        try:
            return Vendor.objects.get(slug=vendor_slug)
        except Vendor.DoesNotExist:
            raise NotFound(detail="Vendor does not exist")
