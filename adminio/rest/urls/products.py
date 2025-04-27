from django.urls import path

from adminio.rest.views import products

urlpatterns = [
    path(
        "/<uuid:product_uid>",
        products.AdminProductDetailsView.as_view(),
        name="admin-product-details",
    ),
    path("", products.AdminProductListView.as_view(), name="admin-product-list"),
]
