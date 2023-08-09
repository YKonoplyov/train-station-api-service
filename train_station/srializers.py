from rest_framework import serializers

from train_station.models import TrainType, Train, Station


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
