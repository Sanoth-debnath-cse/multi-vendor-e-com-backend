from phonenumber_field.serializerfields import PhoneNumberField

from django.contrib.auth import get_user_model

from rest_framework import serializers

from accountio.models import Vendor, VendorUser
from accountio.choices import VendorUserRole

User = get_user_model()


class PublicUserOnboardingSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    last_name = serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    phone = PhoneNumberField(required=True)
    password = serializers.CharField(required=True)
    image = serializers.ImageField(allow_null=True)
    email = serializers.EmailField(allow_null=True)

    def validate_phone(self, phone):
        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError("User already exists!")
        return phone

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class PublicVendorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "uid",
            "slug",
            "created_at",
            "updated_at",
            "name",
            "logo",
            "image",
            "contact_number",
            "website_url",
            "address",
        ]
        read_only_fields = ["uid", "created_at", "updated_at"]


# Onboarding Vendor
class PublicVendorOnboardingSerializer(PublicVendorMiniSerializer):
    owner_first_name = serializers.CharField(
        max_length=50, allow_blank=True, allow_null=True, write_only=True
    )
    owner_last_name = serializers.CharField(
        max_length=50, allow_blank=True, allow_null=True, write_only=True
    )
    owner_phone = PhoneNumberField(required=True, write_only=True)
    owner_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Vendor
        fields = PublicVendorMiniSerializer.Meta.fields + [
            "owner_first_name",
            "owner_last_name",
            "owner_phone",
            "owner_password",
        ]
        read_only_fields = PublicVendorMiniSerializer.Meta.read_only_fields

    def create(self, validated_data):
        # Create user and make that user as an owner to Vendor
        user, _ = User.objects.get_or_create(
            phone=validated_data.get("owner_phone"),
            defaults={
                "first_name": validated_data.get("owner_first_name", ""),
                "last_name": validated_data.get("owner_last_name", ""),
                "password": validated_data.get("owner_password", ""),
            },
        )

        # Create Vendor
        vendor = Vendor.objects.create(
            name=validated_data.get("name"),
            logo=validated_data.get("logo", None),
            image=validated_data.get("image", None),
            contact_number=validated_data.get("contact_number", None),
            website_url=validated_data.get("website_url", None),
            address=validated_data.get("address", None),
        )

        # Create owner
        VendorUser.objects.create(vendor=vendor, user=user, role=VendorUserRole.OWNER)

        return validated_data
