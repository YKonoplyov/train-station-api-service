from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from user.models import User
from train_station.models import TrainType, Train, Station, Route, Trip, Crew


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    ordering = ("email",)


@admin.register(TrainType)
class TrainTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    pass


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    pass


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    pass


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    pass
