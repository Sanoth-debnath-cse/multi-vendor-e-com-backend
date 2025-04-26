from django.urls import path

from productio.rest.views.products import (
    PublicProductListView,
    PublicProductDetailsView,
)

urlpatterns = [
    path(
        "/<slug:product_slug>",
        PublicProductDetailsView.as_view(),
        name="public.product-details",
    ),
    path("", PublicProductListView.as_view(), name="public.product-list"),
]
