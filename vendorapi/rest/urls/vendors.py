from django.urls import path

from vendorapi.rest.views.vendors import (
    PrivateVendorListView,
    PrivateVendorDetailsView,
    PrivateVendorProductListView,
    PrivateVendorProductDetailsView,
)

urlpatterns = [
    path(
        "/<uuid:vendor_uid>/products/<uuid:product_uid>",
        PrivateVendorProductDetailsView.as_view(),
        name="private.vendor-product-details",
    ),
    path(
        "/<uuid:vendor_uid>/products",
        PrivateVendorProductListView.as_view(),
        name="private.vendor-product-list",
    ),
    path(
        "/<uuid:vendor_uid>",
        PrivateVendorDetailsView.as_view(),
        name="private.vendor-details",
    ),
    path("", PrivateVendorListView.as_view(), name="private.vendor-list"),
]
