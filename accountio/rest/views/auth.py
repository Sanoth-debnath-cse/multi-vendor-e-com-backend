from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from accountio.rest.serializers.auth import PublicUserTokenSerializer

class PublicUserTokenView(CreateAPIView):
    serializer_class=PublicUserTokenSerializer
    permission_classes=[AllowAny]