from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView

from productio.models import Product

from productio.rest.serializers.products import PublicProductSerializer

from shared.permissions.admin import IsAdminStaff


class AdminProductListView(ListAPIView):
    serializer_class = PublicProductSerializer
    permission_classes = [IsAdminStaff]
    queryset = Product.objects.select_related("vendor").all()


class AdminProductDetailsView(RetrieveAPIView):
    serializer_class = PublicProductSerializer
    permission_classes = [IsAdminStaff]

    def get_object(self):
        product_uid = self.kwargs["product_uid"]
        try:
            return Product.objects.select_related("vendor").get(uid=product_uid)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found")
