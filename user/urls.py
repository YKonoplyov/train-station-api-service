from django.urls import path

from user.views import CreateUserView, ManageUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("token/", TokenObtainPairView.as_view(), name='generate-token'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token-refresh'),
    path("me/", ManageUserView.as_view(), name="manage-user")
]

app_name = "user"
