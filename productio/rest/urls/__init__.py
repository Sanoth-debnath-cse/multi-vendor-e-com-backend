from django.urls import include, path

urlpatterns = [
    path("", include("productio.rest.urls.products")),
]
