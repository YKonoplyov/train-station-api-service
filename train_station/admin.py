from django.contrib import admin
from train_station.models import TrainType, Train, Station, Route, Trip, Crew

admin.site.register(TrainType)
admin.site.register(Train)
admin.site.register(Station)
admin.site.register(Route)
admin.site.register(Trip)
admin.site.register(Crew)
