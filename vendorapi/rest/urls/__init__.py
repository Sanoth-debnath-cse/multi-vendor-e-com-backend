from django.urls import path, include

urlpatterns = [path("/vendors", include("vendorapi.rest.urls.vendors"))]
