from django.urls import path, include

urlpatterns = [
    path("/orders", include("adminio.rest.urls.orders")),
    path("/products", include("adminio.rest.urls.products")),
]
