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
