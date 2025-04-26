from django.utils import timezone

from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from rest_framework.exceptions import NotFound

from phonenumber_field.serializerfields import PhoneNumberField

User=get_user_model()


class PublicUserTokenSerializer(serializers.Serializer):
    phone=PhoneNumberField(required=True)
    password=serializers.CharField(required=True)
    refresh=serializers.CharField(read_only=True)
    access=serializers.CharField(read_only=True)

    def validate(self, attrs):
        phone=attrs.get("phone")
        if not User.objects.filter(phone=phone).exists():
            raise NotFound(detail="User not found!")
        return attrs
    def create(self, validated_data):
        user= User.objects.get(phone=validated_data.get("phone"))
        refresh=RefreshToken.for_user(user)
        validated_data["refresh"],validated_data["access"]=str(refresh),str(refresh.access_token)

        user.last_login=timezone.now()
        user.save_dirty_fields()

        return validated_data