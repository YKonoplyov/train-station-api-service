from django.urls import path, include
from rest_framework import routers

from train_station.views import (TrainTypeViewSet, TrainViewSet,
                                 StationViewSet)

train_station_router = routers.DefaultRouter()
train_station_router.register("train_types", TrainTypeViewSet)
train_station_router.register("trains", TrainViewSet)
train_station_router.register("stations", StationViewSet)

urlpatterns = [path("", include(train_station_router.urls))]

app_name = "train_station"
