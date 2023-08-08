from django.core.validators import MinValueValidator
from django.db import models


class TrainType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Train(models.Model):
    name = models.CharField(max_length=255)
    cargo_num = models.IntegerField(
        MinValueValidator(1)
    )
    places_in_cargo = models.IntegerField(
        MinValueValidator(1)
    )
    train_type = models.ForeignKey(TrainType, on_delete=models.CASCADE)


class Station(models.Model):
    name = models.CharField(max_length=255, unique=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)

    def __str__(self):
        return self.name


class Route(models.Model):
    source = models.ForeignKey(Station, on_delete=models.CASCADE)
    destination = models.ForeignKey(Station, on_delete=models.CASCADE)
    distance = models.PositiveIntegerField()


class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.DO_NOTHING)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class Crew(models.Model):
    firs_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    trip = models.ManyToManyField(Trip, related_name="crews")
