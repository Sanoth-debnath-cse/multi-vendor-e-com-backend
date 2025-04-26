from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from accountio.rest.views.auth import PublicUserTokenView

urlpatterns=[path("/token",PublicUserTokenView.as_view(),name="auth.token"),
             path("/token/refresh",TokenRefreshView.as_view(),name="auth.refresh.token"),
             ]