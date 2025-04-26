from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated

from accountio.rest.serializers.onboarding import PublicUserOnboardingSerializer

User=get_user_model()

class PublicUserOnboardingView(CreateAPIView):
    serializer_class=PublicUserOnboardingSerializer
    permission_classes=[AllowAny]


class UserList(ListAPIView):
    serializer_class=PublicUserOnboardingSerializer
    permission_classes=[AllowAny]

    def get_queryset(self):
        return User.objects.filter()