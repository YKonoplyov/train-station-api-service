from django.urls import path

from user.views import CreateUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("token/", TokenObtainPairView.as_view(), name='generate-token'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token-refresh'),
]

app_name = "user"
