from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient
from orders.models import Order, Ticket
from train_station.models import Trip, Train, TrainType, Station, Route

ORDER_LIST_URL = reverse("orders:order-list")


class OrderAppTestCase(TestCase):
    def setUp(self):
        self.train_type = TrainType.objects.create(name="Passenger")

        self.train = Train.objects.create(
            name="Test Train",
            cargo_num=10,
            places_in_cargo=100,
            train_type=self.train_type,
        )
        self.station1 = Station.objects.create(
            name="Station A", latitude=1.0, longitude=2.0
        )
        self.station2 = Station.objects.create(
            name="Station B", latitude=3.0, longitude=4.0
        )
        self.route = Route.objects.create(
            source=self.station1, destination=self.station2, distance=200
        )
        self.trip = Trip.objects.create(
            train=self.train,
            route=self.route,
            departure_time=timezone.now() + timezone.timedelta(days=1),
            arrival_time=timezone.now() + timezone.timedelta(days=2),
        )

        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_order_with_valid_tickets(self):
        data = {
            "tickets": [
                {"cargo": 1, "seat": 1, "trip": self.trip.id},
                {"cargo": 1, "seat": 2, "trip": self.trip.id},
            ],
        }
        response = self.client.post(ORDER_LIST_URL, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Ticket.objects.count(), 2)

    def test_create_order_with_invalid_tickets(self):
        data = {
            "tickets": [
                {"cargo": 1, "seat": 200, "trip": self.trip.id},
            ],
        }
        response = self.client.post(ORDER_LIST_URL, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(Ticket.objects.count(), 0)

        data["tickets"] = ({"cargo": 100, "seat": 5, "trip": self.trip.id},)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(Ticket.objects.count(), 0)

    def test_list_orders(self):
        data_1 = {
            "tickets": [
                {"cargo": 1, "seat": 1, "trip": self.trip.id},
                {"cargo": 1, "seat": 2, "trip": self.trip.id},
            ],
        }
        data_2 = {
            "tickets": [
                {"cargo": 1, "seat": 3, "trip": self.trip.id},
            ],
        }
        response = self.client.post(ORDER_LIST_URL, data_1, format="json")
        response = self.client.post(ORDER_LIST_URL, data_2, format="json")
        response = self.client.get(ORDER_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], Order.objects.count())
