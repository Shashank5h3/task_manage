from django.urls import path
from rest_framework_simplejwt.views import (  # type: ignore[import]
    TokenObtainPairView, # it checks whether the user is valid or not and returns the access and refresh token
    TokenRefreshView, # when the access token expires, we can use the refresh token to get a new access token
)

from .views import RegisterView, ProfileView

urlpatterns = [
    path("register/",RegisterView.as_view(),name="register",),
    path("login/",TokenObtainPairView.as_view(),name="login"),
    path("refresh/",TokenRefreshView.as_view(),name="token_refresh"),
    path("profile/",ProfileView.as_view(),name="profile"),
]