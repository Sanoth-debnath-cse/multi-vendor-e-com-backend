from django.urls import path, include

urlpatterns = [path("/orders", include("core.rest.urls.orders"))]
