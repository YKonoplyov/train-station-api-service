from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from train_station.models import TrainType, Train
from train_station.srializers import (TrainTypeSerializer, TrainSerializer,)


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
    serializer_class = TrainSerializer
    queryset = Train.objects.all()