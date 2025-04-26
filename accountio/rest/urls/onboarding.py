from django.urls import path

from accountio.rest.views.onboarding import (
    PublicUserOnboardingView,
    PublicVendorOnboardingView,
    PublicVendorDetailsView,
)

urlpatterns = [
    path(
        "/vendors/<slug:vendor_slug>",
        PublicVendorDetailsView.as_view(),
        name="vendor.details",
    ),
    path("/vendors", PublicVendorOnboardingView.as_view(), name="vendor.onboarding"),
    path("/users", PublicUserOnboardingView.as_view(), name="user.onboarding"),
]
