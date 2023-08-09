from django.urls import path, include
from rest_framework import routers

from train_station.views import TrainTypeViewSet

train_station_router = routers.DefaultRouter()
train_station_router.register(
    "train_types", TrainTypeViewSet
)
urlpatterns = [path("", include(train_station_router.urls))]

app_name = "train_station"
