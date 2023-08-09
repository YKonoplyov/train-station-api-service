from rest_framework import serializers

from train_station.models import TrainType, Train, Station, Route, Trip, Crew


class TrainTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainType
        fields = "__all__"


class TrainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Train
        fields = "__all__"


class TrainListSerializer(TrainSerializer):
    train_type = TrainTypeSerializer(many=False, read_only=True)


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = "__all__"


class RouteListSerializer(RouteSerializer):
    source_station = serializers.CharField(source="source.name")
    destination_station = serializers.CharField(source="destination.name")

    class Meta:
        model = Route
        fields = ("id", "distance", "source_station", "destination_station",)


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = "__all__"


class TripListSerializer(TripSerializer):
    route = serializers.CharField(source="route.__str__")
    train = serializers.CharField(source="train.__str__")

    class Meta:
        model = Trip
        fields = ("id", "departure_time", "arrival_time", "route", "train")


class TripDetailSerializer(TripSerializer):
    route = RouteListSerializer(read_only=True)
    train = TrainSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = "__all__"


class CrewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crew
        fields = "__all__"