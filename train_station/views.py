from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from train_station.models import TrainType, Train, Station, Route, Trip
from train_station.srializers import (TrainTypeSerializer, TrainSerializer,
                                      TrainListSerializer, StationSerializer,
                                      RouteSerializer, RouteListSerializer,
                                      TripSerializer, TripListSerializer,
                                      TripDetailSerializer)


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


class StationViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = StationSerializer
    queryset = Station.objects.all()


class RouteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = RouteListSerializer
    queryset = Route.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return RouteListSerializer
        return RouteSerializer


class TripViewSet(ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TripListSerializer
        if self.action == "retrieve":
            return TripDetailSerializer
        return TripSerializer
