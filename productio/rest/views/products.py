from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from productio.models import Product
from productio.rest.serializers.products import PublicProductSerializer


class PublicProductListView(ListAPIView):
    serializer_class = PublicProductSerializer
    permission_classes = [AllowAny]
    queryset = Product.objects.select_related("vendor").filter(is_active=True)


class PublicProductDetailsView(RetrieveAPIView):
    serializer_class = PublicProductSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        product_slug = self.kwargs["product_slug"]
        try:
            return Product.objects.select_related("vendor").get(slug=product_slug)
        except Product.DoesNotExist:
            raise NotFound(detail="Product does not exist")
