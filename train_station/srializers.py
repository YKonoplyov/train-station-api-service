from rest_framework import serializers

from train_station.models import TrainType, Train, Station, Route


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