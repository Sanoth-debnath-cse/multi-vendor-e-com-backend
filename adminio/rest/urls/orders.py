from django.urls import path

from adminio.rest.views import orders

urlpatterns = [
    path(
        "/<uuid:order_uid>",
        orders.AdminOrderDetailView.as_view(),
        name="admin-product-details",
    ),
    path("", orders.AdminOrderListView.as_view(), name="admin-product-list"),
]
