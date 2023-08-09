from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("user.urls", namespace="user")),
    path(
        "api/train_station/",
        include("train_station.urls", namespace="train_station")
    ),
    path("api/orders/", include("orders.urls", namespace="orders"))
]
