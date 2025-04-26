from django.urls import path

from accountio.rest.views.onboarding import PublicUserOnboardingView,UserList

urlpatterns=[path("/users",PublicUserOnboardingView.as_view(),name="user.onboarding"),
             path("/user/list",UserList.as_view(),name="user.list")]