from django.db import transaction

from rest_framework import serializers

from accountio.models import Vendor

from productio.models import Product


class PrivateVendorListSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        model = Vendor
        fields = [
            "uid",
            "created_at",
            "updated_at",
            "name",
            "logo",
            "image",
            "contact_number",
            "website_url",
            "address",
            "role",
        ]
        read_only_fields = ["uid", "created_at", "updated_at"]


class PrivateVendorProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "uid",
            "created_at",
            "updated_at",
            "name",
            "image",
            "unit_price",
            "total_quantity",
            "is_active",
        ]
        read_only_fields = ["uid", "created_at", "updated_at"]

    @transaction.atomic
    def create(self, validated_data):
        vendor_uid = self.context["view"].kwargs.get("vendor_uid")
        try:
            vendor = Vendor.objects.get(uid=vendor_uid)
        except Vendor.DoesNotExist:
            raise serializers.ValidationError({"detail": "Vendor does not exist"})

        validated_data["vendor"] = vendor

        Product.objects.create(**validated_data)

        return validated_data


class PrivateVendorProductDetailsSerializer(PrivateVendorProductListSerializer):
    class Meta:
        model = Product
        fields = PrivateVendorProductListSerializer.Meta.fields
        read_only_fields = PrivateVendorProductListSerializer.Meta.read_only_fields
        extra_kwargs = {"name": {"required": False}, "unit_price": {"required": False}}
