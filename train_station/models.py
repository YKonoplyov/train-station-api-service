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

    def __str__(self):
        return self.name


class Station(models.Model):
    name = models.CharField(max_length=255, unique=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)

    def __str__(self):
        return self.name


class Route(models.Model):
    source = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="source"
    )
    destination = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="destination"
    )
    distance = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.source}-{self.destination}"


class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.DO_NOTHING)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return (
            f"{self.departure_time} {self.route.source}-"
            f"{self.arrival_time} {self.route.destination}"
        )


class Crew(models.Model):
    firs_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    trip = models.ManyToManyField(Trip, related_name="crews")

    def full_name(self):
        return self.firs_name + self.last_name

    def __str__(self):
        return self.full_name()