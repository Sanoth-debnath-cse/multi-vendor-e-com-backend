from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView

from orderio.models import Order
from vendorapi.rest.serializers.vendors import PrivateOrderListSerializer

from shared.permissions.admin import IsAdminStaff


class AdminOrderListView(ListAPIView):
    serializer_class = PrivateOrderListSerializer
    permission_classes = [IsAdminStaff]
    queryset = Order.objects.prefetch_related("products", "products__vendor").all()


class AdminOrderDetailView(RetrieveAPIView):
    serializer_class = PrivateOrderListSerializer
    permission_classes = [IsAdminStaff]

    def get_object(self):
        order_uid = self.kwargs["order_uid"]

        try:
            return Order.objects.prefetch_related("products", "products__vendor").get(
                uid=order_uid
            )
        except Order.DoesNotExist:
            raise NotFound(detail="Order does not exist")
