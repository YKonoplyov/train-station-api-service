from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from train_station_service import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("user.urls", namespace="user")),
    path(
        "api/train_station/",
        include("train_station.urls", namespace="train_station")
    ),
    path("api/train_station/", include("orders.urls", namespace="orders"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
