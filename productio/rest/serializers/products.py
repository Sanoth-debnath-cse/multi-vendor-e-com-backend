from rest_framework import serializers

from productio.models import Product

from accountio.rest.serializers.onboarding import PublicVendorMiniSerializer


class PublicProductSerializer(serializers.ModelSerializer):
    vendor = PublicVendorMiniSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "uid",
            "slug",
            "name",
            "vendor",
            "unit_price",
            "total_quantity",
            "image",
        ]
        read_only_fields = fields
