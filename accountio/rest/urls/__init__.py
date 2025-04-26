from django.urls import path,include

urlpatterns=[path("/onboarding",include("accountio.rest.urls.onboarding")),
             path("",include("accountio.rest.urls.auth")),
             ]