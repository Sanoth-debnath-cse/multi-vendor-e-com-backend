from django.urls import path

from core.rest.views.orders import UserOrderListView, UserOrderDetailsView

urlpatterns = [
    path(
        "/<uuid:order_uid>", UserOrderDetailsView.as_view(), name="user.order-details"
    ),
    path("", UserOrderListView.as_view(), name="user.order-list"),
]
