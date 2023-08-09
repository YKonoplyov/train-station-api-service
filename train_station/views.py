from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from train_station.models import TrainType, Train, Station, Route, Trip, Crew
from train_station.srializers import (TrainTypeSerializer, TrainSerializer,
                                      TrainListSerializer, StationSerializer,
                                      RouteSerializer, RouteListSerializer,
                                      TripSerializer, TripListSerializer,
                                      TripDetailSerializer, CrewSerializer)


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

    def get_queryset(self):
        queryset = self.queryset.select_related(
            "train",
            "route",
            "route__source",
            "route__destination",
        )
        source = self.request.query_params.get("source")
        destination = self.request.query_params.get("destination")

        if source:
            queryset = queryset.filter(route__source__name__icontains=source)

        if destination:
            queryset = queryset.filter(
                route__destination__name__icontains=destination
            )

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "list":
            return TripListSerializer
        if self.action == "retrieve":
            return TripDetailSerializer
        return TripSerializer


class CrewViewSet(ModelViewSet):
    serializer_class = CrewSerializer
    queryset = Crew.objects.all()
