from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from train_station.models import TrainType, Train, Station, Route, Trip, Crew
from train_station.permissions import IsAdminOrIfAuthenticatedReadOnly
from train_station.srializers import (TrainTypeSerializer, TrainSerializer,
                                      TrainListSerializer, StationSerializer,
                                      RouteSerializer, RouteListSerializer,
                                      TripSerializer, TripListSerializer,
                                      TripDetailSerializer, CrewSerializer,
                                      TrainImageSerializer)


class TrainTypeViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = TrainTypeSerializer
    queryset = TrainType.objects.all()
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class TrainViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = TrainListSerializer
    queryset = Train.objects.all()
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return TrainListSerializer
        if self.action == "upload_image":
            return TrainImageSerializer
        return TrainSerializer

    @action(
        methods=["POST"],
        detail=True,
        url_path="upload-image",
        permission_classes=[IsAdminUser, ]
    )
    def upload_image(self, request, pk=None):
        train = self.get_object()
        serializer = self.get_serializer(train, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StationViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = StationSerializer
    queryset = Station.objects.all()
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class RouteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = RouteListSerializer
    queryset = Route.objects.all()
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


    def get_serializer_class(self):
        if self.action == "list":
            return RouteListSerializer
        return RouteSerializer


class TripViewSet(ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

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
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]
