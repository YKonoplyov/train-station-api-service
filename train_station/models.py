import os.path
import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class TrainType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


def create_train_image_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"
    return os.path.join("uploads/movies/", filename)


class Train(models.Model):
    name = models.CharField(max_length=255)
    cargo_num = models.PositiveIntegerField()
    places_in_cargo = models.PositiveIntegerField()
    train_type = models.ForeignKey(TrainType, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to=create_train_image_path)

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
        Station, on_delete=models.CASCADE, related_name="source_routes"
    )
    destination = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="destination_routes"
    )
    distance = models.PositiveIntegerField()

    @staticmethod
    def validate_route(source, destination, error_to_raise):
        if source.name == destination.name:
            raise error_to_raise(
                "Source and destination should be different places"
            )

    def clean(self):
        self.validate_route(self.source, self.destination, ValidationError)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.full_clean()
        return super(Route, self).save(
            force_insert, force_update, using, update_fields
        )

    def __str__(self):
        return f"{self.source}-{self.destination}"


class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.DO_NOTHING)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    @staticmethod
    def validate_trip(departure_time, arrival_time, error_to_raise):
        now = timezone.now()
        if departure_time < now:
            raise error_to_raise("Departure time can`t be in the past")
        if departure_time > arrival_time:
            raise error_to_raise(
                "Departure time should be earlier than arrival time"
            )

    def clean(self):
        self.validate_trip(
            self.departure_time, self.arrival_time, ValidationError
        )

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.full_clean()

        return super(Trip, self).save(
            force_insert, force_update, using, update_fields
        )

    def __str__(self):
        return (
            f"{self.departure_time} {self.route.source}-"
            f"{self.arrival_time} {self.route.destination}"
        )


class Crew(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    trip = models.ManyToManyField(Trip, related_name="crews")

    def full_name(self):
        return self.firs_name + self.last_name

    def __str__(self):
        return self.full_name()
