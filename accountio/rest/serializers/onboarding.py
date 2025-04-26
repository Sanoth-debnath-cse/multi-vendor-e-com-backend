from phonenumber_field.serializerfields import PhoneNumberField

from django.contrib.auth import get_user_model

from rest_framework import serializers

User=get_user_model()


class PublicUserOnboardingSerializer(serializers.Serializer):
    first_name=serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    last_name=serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    phone=PhoneNumberField(required=True)
    password=serializers.CharField(required=True)
    image=serializers.ImageField(allow_null=True)
    email=serializers.EmailField(allow_null=True)

    def validate_phone(self,phone):
        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError("User already exists!")
        return phone
    def create(self, validated_data):
        user=User.objects.create(**validated_data)
        return user