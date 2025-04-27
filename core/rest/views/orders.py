from rest_framework.exceptions import NotFound
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from core.rest.serializers.orders import UserOrderListSerializer

from orderio.models import Order


class UserOrderListView(ListCreateAPIView):
    serializer_class = UserOrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return (
            Order.objects.prefetch_related("products", "products__vendor")
            .filter(user=user)
            .order_by("-created_at")
        )


class UserOrderDetailsView(RetrieveAPIView):
    serializer_class = UserOrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        order_uid = self.kwargs["order_uid"]
        user = self.request.user

        try:
            return Order.objects.prefetch_related("products", "products__vendor").get(
                uid=order_uid, user=user
            )
        except Order.DoesNotExist:
            raise NotFound(detail="Order does not exist")
