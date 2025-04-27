from rest_framework import serializers

from accountio.models import Vendor


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
            # "contact_number",
            "website_url",
            "address",
            "role",
        ]
        read_only_fields = ["uid", "created_at", "updated_at"]
