from django.urls import path

from vendorapi.rest.views.vendors import PrivateVendorListView, PrivateVendorDetailsView

urlpatterns = [
    path(
        "/<uuid:vendor_uid>",
        PrivateVendorDetailsView.as_view(),
        name="private.vendor-details",
    ),
    path("", PrivateVendorListView.as_view(), name="private.vendor-list"),
]
