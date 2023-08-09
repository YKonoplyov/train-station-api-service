from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from train_station.models import TrainType, Train
from train_station.srializers import (TrainTypeSerializer, TrainSerializer,
                                      TrainListSerializer, )


class TrainTypeViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = TrainTypeSerializer
    queryset = TrainType.objects.all()


class TrainViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = TrainListSerializer
    queryset = Train.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TrainListSerializer
        return TrainSerializer