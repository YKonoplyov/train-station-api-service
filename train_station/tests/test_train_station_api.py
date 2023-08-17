from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from datetime import datetime, timedelta
from train_station.models import TrainType, Train, Station, Route, Trip, Crew


TRAINTYPE_LIST_URL = reverse("train_station:traintype-list")
TRAIN_LIST_URL = reverse("train_station:train-list")
STATION_LIST_URL = reverse("train_station:station-list")
ROUTE_LIST_URL = reverse("train_station:route-list")
CREW_LIST_URL = reverse("train_station:crew-list")
TRIP_LIST_URL = reverse("train_station:trip-list")


class TrainTypeAPITest(APITestCase):
    def setUp(self):
        self.train_type = TrainType.objects.create(name="Passenger")
        self.user = get_user_model().objects.create_superuser(
            email="test@mail.com", password="test12345"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_train_types(self):
        response = self.client.get(TRAINTYPE_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_train_type(self):
        data = {
            "name": "Freight",
        }
        response = self.client.post(TRAINTYPE_LIST_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TrainType.objects.count(), 2)


class TrainAPITest(APITestCase):
    def setUp(self):
        self.train_type = TrainType.objects.create(name="Passenger")
        self.train = Train.objects.create(
            name="Train 1",
            cargo_num=10,
            places_in_cargo=100,
            train_type=self.train_type,
        )
        self.user = get_user_model().objects.create_superuser(
            email="test@mail.com", password="test12345"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_trains(self):
        response = self.client.get(TRAIN_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_train(self):
        data = {
            "name": "New Train",
            "cargo_num": 5,
            "places_in_cargo": 50,
            "train_type": self.train_type.id,
        }
        response = self.client.post(TRAIN_LIST_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Train.objects.count(), 2)


class StationAPITest(APITestCase):
    def setUp(self):
        self.station = Station.objects.create(
            name="Station A", latitude=1.0, longitude=2.0
        )
        self.user = get_user_model().objects.create_superuser(
            email="test@mail.com", password="test12345"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_stations(self):
        response = self.client.get(STATION_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_station(self):
        data = {
            "name": "New Station",
            "latitude": 3.0,
            "longitude": 4.0,
        }
        response = self.client.post(STATION_LIST_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Station.objects.count(), 2)


class RouteAPITest(APITestCase):
    def setUp(self):
        self.station1 = Station.objects.create(
            name="Station A", latitude=1.0, longitude=2.0
        )

        self.station2 = Station.objects.create(
            name="Station B", latitude=3.0, longitude=4.0
        )
        self.route = Route.objects.create(
            source=self.station1, destination=self.station2, distance=200
        )
        self.user = get_user_model().objects.create_superuser(
            email="test@mail.com", password="test12345"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_routes(self):
        response = self.client.get(ROUTE_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_route(self):
        data = {
            "source": self.station1.id,
            "destination": self.station2.id,
            "distance": 300,
        }
        response = self.client.post(ROUTE_LIST_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Route.objects.count(), 2)


class TripAPITest(APITestCase):
    def setUp(self):
        self.station1 = Station.objects.create(
            name="Station A", latitude=1.0, longitude=2.0
        )
        self.station2 = Station.objects.create(
            name="Station B", latitude=3.0, longitude=4.0
        )
        self.train_type = TrainType.objects.create(name="Express")
        self.train = Train.objects.create(
            name="Train 1",
            cargo_num=10,
            places_in_cargo=100,
            train_type=self.train_type,
        )
        self.departure_time = timezone.now() + timedelta(days=1)
        self.arrival_time = self.departure_time + timedelta(hours=2)
        self.route = Route.objects.create(
            source=self.station1, destination=self.station2, distance=200
        )
        self.trip = Trip.objects.create(
            route=self.route,
            train=self.train,
            departure_time=self.departure_time,
            arrival_time=self.arrival_time,
        )
        self.user = get_user_model().objects.create_superuser(
            email="test@mail.com", password="test12345"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_trips(self):
        response = self.client.get(TRIP_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_by_source(self):
        response = self.client.get(
            TRIP_LIST_URL, {"source": self.station1.name}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_by_destination(self):
        response = self.client.get(
            TRIP_LIST_URL, {"destination": self.station2.name}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_trip(self):
        data = {
            "route": self.route.id,
            "train": self.train.id,
            "departure_time": (datetime.now() + timedelta(days=1)),
            "arrival_time": (datetime.now() + timedelta(days=1, hours=2)),
        }
        response = self.client.post(TRIP_LIST_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trip.objects.count(), 2)

    def test_invalid_trip_creation(self):
        data = {
            "route": self.route.id,
            "train": self.train.id,
            "departure_time": (datetime.now() + timedelta(hours=1)),
            "arrival_time": (datetime.now() - timedelta(hours=2)),
        }
        response = self.client.post(TRIP_LIST_URL, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Trip.objects.count(), 1)

    def test_update_trip(self):
        url = reverse("train_station:trip-detail", args=[self.trip.id])
        new_departure_time = self.trip.departure_time + timedelta(hours=1)
        new_arrival_time = self.trip.arrival_time + timedelta(hours=3)
        data = {
            "departure_time": new_departure_time,
            "arrival_time": new_arrival_time,
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.trip.refresh_from_db()
        self.assertEqual(self.trip.departure_time, new_departure_time)
        self.assertEqual(self.trip.arrival_time, new_arrival_time)


class CrewAPITest(APITestCase):
    def setUp(self):
        self.station1 = Station.objects.create(
            name="Station A", latitude=1.0, longitude=2.0
        )
        self.station2 = Station.objects.create(
            name="Station B", latitude=3.0, longitude=4.0
        )
        self.train_type = TrainType.objects.create(name="Express")
        self.train = Train.objects.create(
            name="Train 1",
            cargo_num=10,
            places_in_cargo=100,
            train_type=self.train_type,
        )
        self.departure_time = timezone.now() + timedelta(days=1)
        self.arrival_time = self.departure_time + timedelta(hours=2)
        self.route = Route.objects.create(
            source=self.station1, destination=self.station2, distance=200
        )
        self.trip = Trip.objects.create(
            route=self.route,
            train=self.train,
            departure_time=self.departure_time,
            arrival_time=self.arrival_time,
        )
        self.crew = Crew.objects.create(first_name="John", last_name="Doe")
        self.crew.trip.add(self.trip)
        self.user = get_user_model().objects.create_superuser(
            email="test@mail.com", password="test12345"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_crews(self):
        response = self.client.get(CREW_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_crew(self):
        data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "trip": [self.trip.id],
        }
        response = self.client.post(CREW_LIST_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Crew.objects.count(), 2)
